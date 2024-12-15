
NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
WALL = '#'
EMPTY = '.'
BOX = 'O'
PLAYER = '@'


def read_input():
    with open('input.txt') as f:
        blocks = f.read().split('\n\n')

    grid_raw, movements = blocks[0], list(blocks[1].replace('\n', ''))
    grid = []
    start = [-1, -1]

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


def try_move_box(grid, row, col, dir_row, dir_col):
    start_row, start_col = row, col

    while True:
        row += dir_row
        col += dir_col

        if grid[row][col] == WALL:
            return False

        if grid[row][col] == EMPTY:
            grid[row][col], grid[start_row][start_col] = grid[start_row][start_col], grid[row][col]
            return True


def run():
    grid, start, movements = read_input()

    row = start[0]
    col = start[1]

    print('Initial state:')
    debug_grid(grid, row, col)

    for movement in movements:
        dir_row, dir_col = movement_to_dir(movement)

        row += dir_row
        col += dir_col

        if grid[row][col] == WALL:
            row -= dir_row
            col -= dir_col
            continue

        if grid[row][col] == BOX:
            success = try_move_box(grid, row, col, dir_row, dir_col)
            if not success:
                row -= dir_row
                col -= dir_col
                continue

        # print(f'Move {movement} ({dir_row}, {dir_col}):')
        # debug_grid(grid)

    final_result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == BOX:
                final_result += score(row, col)

    print(f'Part 1: {final_result}')

run()

