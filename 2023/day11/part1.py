from typing import Dict, Tuple
from collections import defaultdict


with open('input.txt', 'r') as f:
    grid = [list(line) for line in f.read().split('\n')]


def rotate_90deg(grid):
    return list(zip(*grid[::-1]))  # cool trick to rotate 2d array 90 deg


# expand galaxies
empty_rows = [i for i, row in enumerate(grid) if all(col == '.' for col in row)]
for i in empty_rows[::-1]:
    grid.insert(i, ['.'] * len(grid[0]))

grid = rotate_90deg(grid)
empty_cols = [i for i, row in enumerate(grid) if all(col == '.' for col in row)]

for i in empty_cols[::-1]:
    grid.insert(i, ['.'] * len(grid[0]))

# rotate back into place
grid = rotate_90deg(grid)
grid = rotate_90deg(grid)
grid = rotate_90deg(grid)

# find all galaxy coordinates
galaxies_arr = []

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '#':
            galaxies_arr.append((row, col))
galaxies = { v: i for i, v in enumerate(galaxies_arr)}
galaxies_reversed = { v: i for i, v in enumerate(galaxies_arr)}

# for each galaxy, BFS till all scanned
pairs: Dict[Tuple[int, int], int] = defaultdict(int)
for i, (start_row, start_col) in enumerate(galaxies):
    print(f'Galaxy {i + 1} of {len(galaxies_arr)}')
    seen = set()
    q = [(start_row, start_col, 0)]
    while q:
        row, col, depth = q.pop(0)
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            continue
        if (row, col) in seen:
            continue
        seen.add((row, col))

        if grid[row][col] == '#' and (row, col) in galaxies_reversed:
            j = galaxies_reversed[(row, col)]
            if i != j:
                lower, higher = min(i, j), max(i, j)
                pairs[(lower, higher)] = depth

        for delta_row, delta_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_row, new_col = row + delta_row, col + delta_col
            q.append((new_row, new_col, depth + 1))

result = sum(pairs.values())
print(f'Part 1: {result}')