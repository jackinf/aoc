from dataclasses import dataclass
from typing import Tuple, List, Optional

Board = List[List[str]]

rock_shape1 = [
    ['@', '@', '@', '@']
]

rock_shape2 = [
    ['.', '@', '.'],
    ['@', '@', '@'],
    ['.', '@', '.'],
]

rock_shape3 = [
    ['.', '.', '@'],
    ['.', '.', '@'],
    ['@', '@', '@'],
]

rock_shape4 = [
    ['@'],
    ['@'],
    ['@'],
    ['@'],
]

rock_shape5 = [
    ['@', '@'],
    ['@', '@'],
]

all_spawn_rock_shapes = [rock_shape1, rock_shape2, rock_shape3, rock_shape4, rock_shape5]
max_possible_height = max(len(x) for x in all_spawn_rock_shapes)


def peek_next_shape():
    return all_spawn_rock_shapes[0]

def get_next_spawn_rock_shape_height():
    next_shape = (all_spawn_rock_shapes[0])
    return len(next_shape)


@dataclass
class FallingRock:
    row: int
    col: int
    shape: List[List[str]]

    @property
    def width(self):
        return len(self.shape[0])

    @property
    def height(self):
        return len(self.shape)

    def move_horizontally(self, by: int):
        self.col += by

    def move_vertically(self, by: int):
        self.row += by


class Grid:
    board: List[List[str]] = []
    curr_spawn_rock_coord = (3, 2)
    falling_rock: Optional[FallingRock] = None
    rocks_spawned: int = 0

    def __init__(self):
        pass

    def expand_board(self, desired_height: int):
        # grid is 7 units wide (height is unlimited)
        while len(self.board) <= desired_height:
            self.board.append(['.' for _ in range(7)])

    def try_spawn_rock(self):
        if self.falling_rock is not None:
            return False

        row, col = self.curr_spawn_rock_coord
        shape = all_spawn_rock_shapes.pop(0)
        self.falling_rock = FallingRock(row=row, col=col, shape=shape)

        all_spawn_rock_shapes.append(shape)
        self.rocks_spawned += 1
        return True

    def update(self, move_dir: int):
        assert move_dir == 1 or move_dir == -1

        self.falling_rock.move_horizontally(move_dir)
        if self.__falling_rock_intersects():
            self.falling_rock.move_horizontally(-move_dir)  # undo

        self.falling_rock.move_vertically(-1)
        if self.__falling_rock_intersects():
            self.falling_rock.move_vertically(1)  # undo
            self.__place_a_falling_rock()

    def get_cached(self):
        return ''.join([x for y in self.board[-8:] for x in y])

    def draw(self):
        self.__clear_board()

        # draw a falling rock shape
        if self.falling_rock:
            rock = self.falling_rock
            for row in range(rock.height):
                for col in range(rock.width):
                    self.board[rock.row - row][rock.col + col] = rock.shape[row][col]

        # output everything
        for row in range(len(self.board) - 1, -1, -1):
            print('|', end='')
            for col in range(len(self.board[0])):
                print(self.board[row][col], end='')
            print('|', end='')
            print()
        print('+-------+')

        self.__clear_board()

    def get_first_n_rows(self, n):
        if len(self.board) < n:
            return ''
        self.__clear_board()

        output = ""

        # draw a falling rock shape
        if self.falling_rock:
            rock = self.falling_rock
            for row in range(rock.height):
                for col in range(rock.width):
                    self.board[rock.row - row][rock.col + col] = rock.shape[row][col]

        # output everything
        for row in range(len(self.board) - 1, len(self.board) - n, -1):
            output += "|"
            for col in range(len(self.board[0])):
                output += self.board[row][col]

        self.__clear_board()
        return output

    def get_height(self):
        for row in range(len(self.board) - 1, -1, -1):
            for col in range(len(self.board[0])):
                if self.board[row][col] != '.':
                    return row + 1
        return 0


    def __clear_board(self):
        for row in range(len(self.board) - 1, -1, -1):
            for col in range(len(self.board[0])):
                if self.board[row][col] != '#':
                    self.board[row][col] = '.'

    def __falling_rock_intersects(self) -> bool:
        rock: FallingRock = self.falling_rock
        for row in range(rock.height):
            for col in range(rock.width):
                if not (0 <= col < rock.width and 0 <= row < rock.height):
                    return True

                if not (0 <= rock.row - row < len(self.board) and 0 <= rock.col + col < len(self.board[0])):
                    return True

                if self.board[rock.row - row][rock.col + col] != '.' and rock.shape[row][col] != '.':
                    return True

        return False

    def __place_a_falling_rock(self):
        rock: FallingRock = self.falling_rock
        for row in range(rock.height):
            for col in range(rock.width):
                symbol = "#" if rock.shape[row][col] == "@" else self.board[rock.row - row][rock.col + col]
                self.board[rock.row - row][rock.col + col] = symbol
        self.falling_rock = None
        self.__recalculate_spawn_position()

    def __recalculate_spawn_position(self):
        safety_offset = 0  # just in case
        spawn_row, spawn_col = self.curr_spawn_rock_coord

        next_shape = peek_next_shape()
        row_offset = 3
        shape_height = len(next_shape)

        for row in range(len(self.board)-1, -1, -1):
            for col in range(len(self.board[0])):
                if self.board[row][col] != '.':
                    new_start_row = row + row_offset + shape_height
                    self.expand_board(new_start_row + safety_offset)
                    self.curr_spawn_rock_coord = (new_start_row, spawn_col)
                    return


if __name__ == '__main__':
    with open('input.txt') as f:
        arrows = f.readline().strip()
        movement_map = {'>': 1, '<': -1}
        movements = [movement_map[arrow] for arrow in arrows]

    grid = Grid()
    grid.expand_board(10)

    global_i = 0
    cache = {}
    target = 1_000_000_000_000

    """
    I am trying to check if the state has been repeated somehow...
    
    I found that each 5000 steps falls exactly 835 rocks
    That means when we reach 1_000_000_000_000, then 835 rocks will fall 1_000_000_000_000 / 5000 = 2_000_000_000 times
    therefore, a total amount of rocks that will fall will be 2_000_000_000 x 835 =...
    
    Ok, that seems to be the wrong assumption...    
    """

    skip_height = 0
    skip_rocks = 0

    while True:
        local_i = global_i % len(movements)
        movement = movements[local_i]
        height_now = grid.get_height()

        print(f'\r'
              f'global index now={global_i}, '
              f'local index before & now={local_i}, '
              f'rocks spawned now={skip_rocks + grid.rocks_spawned}, '
              f'tower height now={skip_height + height_now}, '
              , end='', flush=True)

        if skip_rocks + grid.rocks_spawned == target:
            print(f'\nResult 2: {skip_height + height_now}')  # guessed 1535483870964 (too high), 1535483870918 (too low)
            break
        elif skip_rocks + grid.rocks_spawned > target:
            print('fail')
            break

        is_rock_spawned = grid.try_spawn_rock()

        if is_rock_spawned and skip_height == 0:
            n_rows_output = grid.get_first_n_rows(100)  # check top 100 rows (if there are not enough rows, then '')
            if n_rows_output:
                key = (n_rows_output, local_i)

                # check if the state is the same state has been seen before, the set of movements is going to be the same, and
                if key in cache:
                    global_i_before, rocks_spawned_before, height_before = cache[key]
                    global_i_delta = global_i - global_i_before
                    rocks_spawned_delta = grid.rocks_spawned - rocks_spawned_before
                    height_delta = height_now - height_before
                    print(f'\nFound the same state: '
                          f'global index before={global_i_before}, '
                          f'global index now={global_i}, '
                          f'global index delta={global_i_delta}, '
                          f'local index before & now={local_i}, '
                          f'rocks spawned before={rocks_spawned_before}, '
                          f'rocks spawned now={grid.rocks_spawned}, '
                          f'rocks spawned delta={rocks_spawned_delta}',
                          f'tower height before={height_before}, '
                          f'tower height now={height_now}, '
                          f'tower height delta={height_delta}',
                          )

                    # magic... not sure what to do here...
                    steps_to_skip = (target // rocks_spawned_delta) - len(movements)
                    global_i *= steps_to_skip
                    skip_height = steps_to_skip * height_delta
                    skip_rocks = steps_to_skip * rocks_spawned_delta

                cache[key] = (global_i, grid.rocks_spawned, height_now)

        grid.update(movement)
        global_i += 1

    # global_i_delta (200)
    # rock spawn delta (35)
    # tower height delta (53)
    # at global_i 609, rocks 109, height is 170
    # at global_i 809, rocks 144, height is 223
    # ...
    # at rocks 1 million-million the height is ?

