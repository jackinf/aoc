import sys

with open('input.txt') as f:
    grid = [list(x) for x in f.read().splitlines()]

# find x,y position of ^ character
cx, cy = next((y, x) for y, row in enumerate(grid) for x, val in enumerate(row) if val == '^')
grid[cx][cy] = '.'

# horizontal-vertical directions; current direction
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_index = 0

def debug_grid():
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print('X' if (row, col) in visited else grid[row][col], end='')
        print()


visited = set()
while True:
    visited.add((cx, cy))

    # find the next empty cell
    # if the next cell is out of bounds then we finish
    # if the next cell is wall, then rotate & continue searching
    # if the next cell is empty space, exit the inner-loop
    while True:
        dx, dy = directions[dir_index]
        nx, ny = cx + dx, cy + dy

        # check if out of bounds; if yes - finish
        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
            print(f'Part 1: {len(visited)}')
            debug_grid()
            sys.exit()

        if grid[nx][ny] == '#':
            dir_index += 1
            dir_index %= len(directions)
            continue

        if grid[nx][ny] == '.':
            cx, cy = nx, ny
            break

        raise Exception('unsupported cell type')

