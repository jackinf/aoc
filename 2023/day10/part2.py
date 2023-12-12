from pprint import pprint

RIGHT, LEFT, UP, DOWN = (0, 1), (0, -1), (-1, 0), (1, 0)
tiles_count = 0
with open('sample5.txt') as f:
    grid = [list(row) for row in f.read().split('\n')]


def is_oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


def find_start_dir(grid, row, col):
    for dr, dc, valid in ((0, -1, {'-', 'L', 'F'}), (-1, 0, {'|', '7', 'F'}), (1, 0, {'|', 'L', 'J'}), (0, 1, {'-', 'J', '7'})):
        next_row, next_col = row + dr, col + dc

        if is_oob(grid, next_row, next_col):
            continue

        print(next_col, next_row)
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
    return (next_row, next_col), (next_dir_row, next_dir_col)


start_row, start_col = find_starting_pos(grid)
curr_row, curr_col = start_row, start_col
(curr_dir_col, curr_dir_row) = find_start_dir(grid, start_row, start_col)

seen = set()

while True:
    (curr_row, curr_col), (curr_dir_row, curr_dir_col) = step(grid, curr_row, curr_col, curr_dir_row, curr_dir_col)

    seen.add((curr_row, curr_col))
    # grid[curr_row][curr_col] = 'X'

    if (curr_row, curr_col) == (start_row, start_col):
        break


def outermost_coordinates(grid):
    rows, cols = len(grid), len(grid[0])
    return [(r, c) for r in range(rows) for c in range(cols) if r in [0, rows-1] or c in [0, cols-1]]


def find_gaps(grid):
    gaps = set()
    for i in range(len(grid) - 1):
        for j in range(len(grid[0]) - 1):
            left, right = grid[i][j], grid[i][j + 1]
            up, down = grid[i][j], grid[i + 1][j]

            if left in {'|', '7', 'J'} and right in {'|', 'F', 'L'}:
                x1 = (min(i, j), max(i, j))
                x2 = (min(i, j + 1), max(i, j + 1))
                gaps.add((x1, x2))
            if up in {'-', 'J', 'L'} and down in {'-', 'F', '7'}:
                x1 = min(i, j), max(i, j)
                x2 = (min(i + 1, j), max(i + 1, j))
                gaps.add((x1, x2))

    return gaps


gaps = find_gaps(grid)
pprint(gaps)


for row, col in outermost_coordinates(grid):
    q = [(row, col)]
    gap_q = []
    while q:
        curr_row, curr_col = q.pop(0)
        if is_oob(grid, curr_row, curr_col):
            continue
        if (curr_row, curr_col) in seen:
            continue
        seen.add((curr_row, curr_col))
        grid[curr_row][curr_col] = '#'

        for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
            next_row, next_col = curr_row + delta_row, curr_col + delta_col
            q.append((next_row, next_col))

# debugging
for row in range(len(grid)):
    print()
    for col in range(len(grid[0])):
        print(grid[row][col], end="")
print()

tiles_count = len([x for y in grid for x in y if x != "#" and x != 'X'])

print(f'Part 2: {tiles_count}')
