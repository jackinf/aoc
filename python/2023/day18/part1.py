with open('input.txt', 'r') as f:
    directions = [line.split() for line in f.read().split('\n')]
    directions = [(line[0], int(line[1]), line[2][1:-1]) for line in directions]


def debug(grid):
    for row in range(len(grid)):
        print()
        for col in range(len(grid[0])):
            print(str(grid[row][col]), end="")
    print()


dir_map = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0)
}

path = [(0, 0)]
for direction in directions:
    symbol, steps, color = direction

    delta_row, delta_col = dir_map[symbol]
    for _ in range(steps):
        cell = path[-1][0] + delta_row, path[-1][1] + delta_col
        path.append(cell)

left = min(cell[1] for cell in path) - 1  # -1 so that there is an outer layer on the left
up = min(cell[0] for cell in path) - 1  # -1 so that there is an outer layer on the top

# apply offset
for i in range(len(path)):
    path[i] = path[i][0] - up, path[i][1] - left

COLS = max(cell[1] for cell in path) + 2  # +1 is mandatory to include last element, and another +1 so that there is an outer layer on the right
ROWS = max(cell[0] for cell in path) + 2  # +1 is mandatory to include last element, and another +1 so that there is an outer layer on the bottom

# create grid
grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]
path = set(path)
for i, (row1, col1) in enumerate(path):
    grid[row1][col1] = '#'

q = [(0, 0)]
while q:
    row, col = q.pop(0)
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        continue

    if grid[row][col] != '.':
        continue
    grid[row][col] = 'x'

    q.append((row + 1, col))
    q.append((row - 1, col))
    q.append((row, col + 1))
    q.append((row, col - 1))

# debug(grid)
total = len([x for y in grid for x in y if x != 'x'])
print(f'Part 1: {total}')