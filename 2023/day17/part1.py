import sys
from collections import defaultdict
import heapq

# FAIL
with open('input.txt', 'r') as f:
    grid = [list(map(int, list(line))) for line in f.read().split('\n')]


def is_oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


def debug(grid, seen):
    for row in range(len(grid)):
        print()
        for col in range(len(grid[0])):

            if (row, col) in seen:
                print(str(grid[row][col]), end='')
            else:
                print('.', end='')
    print()



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


seen = defaultdict(lambda: float('inf'))
best_row, best_col = 0, 0
q = []
COUNTER = 3
q.append((-grid[0][0], 0, 0, (1, 0), COUNTER))
q.append((-grid[0][0], 0, 0, (0, 1), COUNTER))
moves = 0
while q:
    moves += 1
    heat, row, col, dir, counter = heapq.heappop(q)
    row, col = -row, -col

    best_row = max(best_row, row)
    best_col = max(best_col, col)
    print(f'q len = {len(q)}, best_row = {best_row} / {len(grid)}, best_col = {best_col} / {len(grid[0])}', end='\r')

    if counter <= 0:
        continue

    if is_oob(grid, row, col):
        continue

    heat += grid[row][col]

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        print(f'Part 1: {heat}, moves: {moves}')
        sys.exit()

    key = (row, col, counter)
    if seen[key] < heat:
        continue
    seen[key] = heat

    # move forward
    heapq.heappush(q, (heat, -(row + dir[0]), -(col + dir[1]), dir, (counter - 1)))

    # turn left
    new_dir1 = turn_90deg_neg[dir]
    heapq.heappush(q, (heat, -(row + new_dir1[0]), -(col + new_dir1[1]), new_dir1, 3))

    # turn right
    new_dir2 = turn_90deg[dir]
    heapq.heappush(q,(heat, -(row + new_dir2[0]), -(col + new_dir2[1]), new_dir2, 3))




