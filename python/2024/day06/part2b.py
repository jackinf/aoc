import os
import copy

filepath = os.path.join(os.getcwd(), 'sample1.txt')

with open('python/2024/day06/sample1.txt') as f:
    lines = f.readlines()
    grid = [list(x) for x in lines]

# start = [(i, j) for i, row in enumerate(grid) for j in i, row in enumerate(row) if val == '^']
cx, cy = next((y, x) for y, row in enumerate(grid) for x, val in enumerate(row) if val == '^')
grid[cx][cy] = '.'
start_x, start_y = cx, cy
            
WALL = '#'
EMPTY = '.'
LIMIT = 1000
N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)
directions = [N, E, S, W]
direction_index = 0

grid[start_x][start_y] = EMPTY


def debug_grid():
    """Print the grid with successful enclosures marked."""
    print()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in results:
                print('O', end='')
            else:
                print(grid[row][col], end='')
        print()
    print('====')
    print()


def check_if_loop(grid2, direction_index2, limit, row, col):
    curr_row2, curr_col2 = row, col
    limit2 = limit
    while True:
        limit2 -= 1
        if limit2 == 0:
            return True

        d_row, d_col = directions[direction_index2]
        next_row2, next_col2 = curr_row2 + d_row, curr_col2 + d_col

        if not (0 <= next_row2 < len(grid2) and 0 <= next_col2 < len(grid[0])):
            return False

        if grid[next_row2][next_col2] == WALL:
            direction_index2 = (direction_index2 + 1) % len(directions)
            continue

        if grid[next_row2][next_col2] == EMPTY:
            curr_row2, curr_col2 = next_row2, next_col2


curr_row, curr_col = start_x, start_y
results = set()
while True:
    d_row, d_col = directions[direction_index]
    next_row, next_col = curr_row + d_row, curr_col + d_col
    # print(f'row = {next_row}, col = {next_col}')
    # print(grid[next_row][next_col])

    if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
        break

    if grid[next_row][next_col] == WALL:
        direction_index = (direction_index + 1) % len(directions)
        continue

    if grid[next_row][next_col] == EMPTY:
        # grid2 = copy.deepcopy(grid)
        grid[next_row][next_col] = WALL
        direction_index2 = (direction_index + 1) % len(directions)
        is_loop = check_if_loop(grid, direction_index2, LIMIT, curr_row, curr_col)
        if is_loop:
            results.add((next_row, next_col))
        grid[next_row][next_col] = EMPTY

        curr_row, curr_col = next_row, next_col

print(results)
debug_grid()
print(f'Part 2: {len(results)}')

