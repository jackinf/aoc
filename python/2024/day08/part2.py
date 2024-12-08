from collections import defaultdict

with open('python/2024/day08/sample.txt') as f:
# with open('python/2024/day08/input.txt') as f:
    lines = f.read().split('\n')
    grid = [list(line) for line in lines]

M, N =len(grid), len(grid[0])

# find coordinates
type_coords = defaultdict(set)
for row_i, row in enumerate(grid):
    for col_i, val in enumerate(row):
        x, y = min(row_i, col_i), max(row_i, col_i)
        type_coords[val].add((row_i, col_i))

del type_coords['.']

# find pairs
pairs = defaultdict(list)
for type, coords in type_coords.items():
    coords = list(coords)
    for i in range(len(coords) - 1):
        coord1 = coords[i]
        for j in range(i + 1, len(coords)):
            coord2 = coords[j]
            pairs[type].append((coord1, coord2))

# calculate distance between each pair
results = set()
for type, type_pairs in pairs.items():
    for (x1, y1), (x2, y2) in type_pairs:
        xd, yd = x1 - x2, y1 - y2

        nx1, ny1 = x1 + xd, y1 + yd
        # results.add((type, nx1, ny1))   
        while 0 <= nx1 < M and 0 <= ny1 < N:
            results.add((type, nx1, ny1))    
            nx1, ny1 = nx1 + xd, ny1 + yd
        
        nx2, ny2 = x2 - xd, y2 - yd
        # results.add((type, nx2, ny2))
        while 0 <= nx2 < M and 0 <= ny2 < N:
            results.add((type, nx2, ny2))
            nx2, ny2 = nx2 - xd, ny2 - yd
        

# remove out of bounds
results2 = set()
for type, row, col in results:
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        continue
 
    grid[row][col] = '#'
    results2.add((row, col))


def debug_grid():
    for row in range(M):
        for col in range(N):
            val = grid[row][col]
            print(val, end='')
        print()


debug_grid()

print(f'Part 2: {len(results)}')

with open('output.txt', 'w') as f:
    for line in grid:
        f.write(''.join(line))
        f.write('\n')

'''
expected
##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##

actual
##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....#....#..
.#...##....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
'''