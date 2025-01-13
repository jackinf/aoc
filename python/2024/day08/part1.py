from collections import defaultdict
from pprint import pprint

# with open('sample.txt') as f:
with open('sample1.txt') as f:
    lines = f.read().split('\n')
    grid = [list(line) for line in lines]

M, N = len(grid), len(grid[0])

# find coordinates
type_coords = defaultdict(set)
for row_i, row in enumerate(grid):
    for col_i, val in enumerate(row):
        x, y = min(row_i, col_i), max(row_i, col_i)
        type_coords[val].add((row_i, col_i))

del type_coords['.']

print("type_coords")
pprint(type_coords)

# find pairs
pairs = defaultdict(list)
for type, coords in type_coords.items():
    coords = list(coords)
    for i in range(len(coords) - 1):
        coord1 = coords[i]
        for j in range(i + 1, len(coords)):
            coord2 = coords[j]
            pairs[type].append((coord1, coord2))

print("pairs")
pprint(pairs)

# calculate distance between each pair
results = set()
for type, type_pairs in pairs.items():
    for (x1, y1), (x2, y2) in type_pairs:
        xd, yd = x1 - x2, y1 - y2
        nx1, ny1 = x1 + xd, y1 + yd
        nx2, ny2 = x2 - xd, y2 - yd
        results.add((type, nx1, ny1))
        results.add((type, nx2, ny2))

print("results")
pprint(results)

# remove out of bounds
results2 = set()
for type, row, col in results:
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        continue
 
    grid[row][col] = '#'
    results2.add((row, col))

print("results2")
pprint(results2)

def debug_grid():
    for row in range(M):
        for col in range(N):
            val = grid[row][col]
            print(val, end='')
        print()


debug_grid()

print(f'Part 1: {len(results2)}')
