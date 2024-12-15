
NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
WALL = '#'
EMPTY = '.'
BOX = 'O'
BOX_L = '['
BOX_R = ']'
PLAYER = '@'
DEBUG = False


def read_input():
    with open('input.txt') as f:
        blocks = f.read().split('\n\n')

    grid_raw, movements = blocks[0], list(blocks[1].replace('\n', ''))
    grid = []
    start = [-1, -1]

    grid_raw = (grid_raw
        .replace(WALL, WALL + WALL)
        .replace(BOX, BOX_L + BOX_R)
        .replace(EMPTY, EMPTY + EMPTY)
        .replace(PLAYER, PLAYER + EMPTY))

    for row_index, row in enumerate(grid_raw.split('\n')):
        grid.append([])
        for col_index, val in enumerate(row):
            if val == PLAYER:
                start = [row_index, col_index]
                grid[-1].append(EMPTY)
            else:
                grid[-1].append(val)

    return grid, start, movements


def score(row, col) -> int:
    return row * 100 + col


def debug_grid(grid, player_row, player_col):
    if not DEBUG:
        return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == player_row and col == player_col:
                print(PLAYER, end='')
            else:
                print(grid[row][col], end='')
        print()


def movement_to_dir(symbol: str):
    match symbol:
        case '<': return WEST
        case '^': return NORTH
        case 'v': return SOUTH
        case '>': return EAST
    raise Exception('nope')


def can_move_horizontally(grid, row, col, dir_col):
    if grid[row][col] == EMPTY:
        return True

    if grid[row][col] == WALL:
        return False

    return can_move_horizontally(grid, row, col + dir_col, dir_col)


def move_horizontally(grid, row, col, dir_col, temp):
    temp, grid[row][col] = grid[row][col], temp

    if temp == EMPTY:
        return

    move_horizontally(grid, row, col + dir_col, dir_col, temp)


def can_move_vertically(grid, row, col, dir_row):
    # base case: happy flow
    if grid[row][col] == EMPTY:
        return True

    # base case: sad flow
    if grid[row][col] == WALL:
        return False

    if grid[row][col] == BOX_L:
        left = can_move_vertically(grid, row + dir_row, col, dir_row)
        right = can_move_vertically(grid, row + dir_row, col + 1, dir_row)

        return left and right

    if grid[row][col] == BOX_R:
        left = can_move_vertically(grid, row + dir_row, col, dir_row)
        right = can_move_vertically(grid, row + dir_row, col - 1, dir_row)

        return left and right

    raise Exception('Not supported symbol')


def move_vertically(grid, row, col, dir_row, temp):
    temp, grid[row][col] = grid[row][col], temp

    if temp == EMPTY:
        return

    if temp == BOX_L:
        grid[row][col + 1] = EMPTY
        move_vertically(grid, row + dir_row, col, dir_row, BOX_L)
        move_vertically(grid, row + dir_row, col + 1, dir_row, BOX_R)
        return

    if temp == BOX_R:
        grid[row][col - 1] = EMPTY
        move_vertically(grid, row + dir_row, col - 1, dir_row, BOX_L)
        move_vertically(grid, row + dir_row, col, dir_row, BOX_R)
        return


def try_move_box(grid, row, col, dir_row, dir_col):
    # move horizontally
    if dir_col != 0 and dir_row == 0:
        can_move = can_move_horizontally(grid, row, col, dir_col)
        if can_move:
            move_horizontally(grid, row, col, dir_col, EMPTY)
        return can_move


    # move vertically
    if dir_col == 0 and dir_row != 0:
        can_move = can_move_vertically(grid, row, col, dir_row)
        if can_move:
            move_vertically(grid, row, col, dir_row, EMPTY)
        return can_move

    raise Exception('no diagonal or 0,0 movements!')


def run():
    grid, start, movements = read_input()

    row = start[0]
    col = start[1]

    if DEBUG:
        print('Initial state:')
    debug_grid(grid, row, col)

    for movement in movements:
        dir_row, dir_col = movement_to_dir(movement)

        next_row, next_col = row + dir_row, col + dir_col

        if grid[next_row][next_col] == WALL:
            debug_grid(grid, row, col)
        elif grid[next_row][next_col] == EMPTY:
            row = next_row
            col = next_col
            debug_grid(grid, row, col)
        elif grid[next_row][next_col] == BOX_L or grid[next_row][next_col] == BOX_R:
            success = try_move_box(grid, next_row, next_col, dir_row, dir_col)
            if success:
                row = next_row
                col = next_col

        if DEBUG:
            print(f'Move {movement} ({dir_row}, {dir_col}):')
        debug_grid(grid, row, col)


    final_result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == BOX_L:
                final_result += score(row, col)

    print(f'Part 2: {final_result}')

run()

