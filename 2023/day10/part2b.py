from pprint import pprint

# FAIL
RIGHT, LEFT, UP, DOWN = (0, 1), (0, -1), (-1, 0), (1, 0)
step_count = 0
with open('sample2.txt') as f:
    grid = [list(row) for row in f.read().split('\n')]


def is_oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


def find_start_dir(grid, row, col):
    for dr, dc, valid in ((0, -1, {'-', 'L', 'F'}), (-1, 0, {'|', '7', 'F'}), (1, 0, {'|', 'L', 'J'}), (0, 1, {'-', 'J', '7'})):
        next_row, next_col = row + dr, col + dc

        if is_oob(grid, next_row, next_col):
            continue

        if grid[next_row][next_col] not in valid:
            continue

        return dc, dr

    raise Exception('not found')


def map_dir(symbol: str, dir_row, dir_col):
    match symbol, (dir_row, dir_col):
        case 'S', _: return 0, 0
        case 'J', (0, 1): return -1, 0
        case 'J', (1, 0): return 0, -1
        case 'L', (0, -1): return -1, 0
        case 'L', (1, 0): return 0, 1
        case '7', (-1, 0): return 0, -1
        case '7', (0, 1): return 1, 0
        case 'F', (-1, 0): return 0, 1
        case 'F', (0, -1): return 1, 0
        case '|', (-1, 0): return -1, 0
        case '|', (1, 0): return 1, 0
        case '-', (0, -1): return 0, -1
        case '-', (0, 1): return 0, 1

    raise Exception('cannot map')


def find_starting_pos(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                return row, col
    raise Exception('starting pos not found')


def step(grid, row, col, dir_row, dir_col):
    next_row, next_col = row + dir_row, col + dir_col
    (next_dir_row, next_dir_col) = map_dir(grid[next_row][next_col], dir_row, dir_col)

    global step_count
    step_count += 1

    return (next_row, next_col), (next_dir_row, next_dir_col)


def debug_grid(grid):
    # debugging
    for row in range(len(grid)):
        print()
        for col in range(len(grid[0])):
            print(grid[row][col], end="")
    print()


connections = {
    'J': ((-1, 0), (0, -1)),
    'L': ((-1, 0), (0, 1)),
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'F': ((0, 1), (1, 0)),
    '7': ((0, -1), (1, 0)),
}

# debug_grid(grid)


start_row, start_col = find_starting_pos(grid)
curr_row, curr_col = start_row, start_col
(curr_dir_col, curr_dir_row) = find_start_dir(grid, start_row, start_col)


turn_90deg = {
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0)
}

turn_90deg_neg = {
    (1, 0): (0, 1),
    (0, -1): (1, 0),
    (-1, 0): (0, -1),
    (0, 1): (-1, 0)
}

seen = set()
while True:
    (curr_row, curr_col), (curr_dir_row, curr_dir_col) = step(grid, curr_row, curr_col, curr_dir_row, curr_dir_col)
    seen.add((curr_row, curr_col))

    if (curr_row, curr_col) == (start_row, start_col):
        break


# remove junk
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if (row, col) not in seen and grid[row][col] in {'-', '|', '7', 'L', 'J', 'F'}:
            grid[row][col] = '.'

# debug_grid(grid)

counts = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
for row in range(len(grid)):
    inside = False
    for col in range(len(grid[0])):
        val = grid[row][col]
        if val == '.' and inside:
            counts[row][col] = True
            continue

        if val in ('7', '|', 'J', 'F', 'L', 'S'):
            inside = not inside


debug_grid(grid)

total = len([x for y in counts for x in y if x])

print(f'Part 2: {total}')
# 5705
# 275 - too high