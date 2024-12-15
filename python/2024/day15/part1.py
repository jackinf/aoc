
NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
WALL = '#'
EMPTY = '.'
BOX = 'O'


def read_input():
    with open('input.txt') as f:
        blocks = f.read().split('\n\n')

    grid_raw, movements = blocks[0], list(blocks[1].replace('\n', ''))
    grid = []
    start = [-1, -1]

    for row_index, row in enumerate(grid_raw.split('\n')):
        grid.append([])
        for col_index, val in enumerate(row):
            grid[-1].append(val)

            if val == '@':
                start = [row_index, col_index]

    return grid, start, movements


def score(row, col) -> int:
    return row * 100 + col


def movement_to_dir(symbol: str):
    match symbol:
        case '<': return WEST
        case '^': return NORTH
        case 'v': return SOUTH
        case '>': return EAST
    raise Exception('nope')


def try_move_box(grid, row, col, dir_row, dir_col):
    start_row, start_col = row, col

    while grid[row][col] != WALL:
        row += dir_row
        col += dir_col

        if grid[row][col] == EMPTY:
            grid[row][col], grid[start_row][start_col] = grid[start_row][start_col], grid[row][col]
            return True

    return False


def run():
    grid, start, movements = read_input()

    row = start[0]
    col = start[1]

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

    final_result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == BOX:
                final_result += score(row, col)

    print(f'Part 1: {final_result}')
    # attempted 1559091 - too low

run()

