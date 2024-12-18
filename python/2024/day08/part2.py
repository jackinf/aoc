from collections import defaultdict

def read_input():
    with open('input.txt') as f:
        # with open('input.txt') as f:
        lines = f.read().split('\n')
        grid = [list(line) for line in lines]

    return grid


def find_coordinates(grid):
    type_coords = defaultdict(set)
    for row_i, row in enumerate(grid):
        for col_i, val in enumerate(row):
            # x, y = min(row_i, col_i), max(row_i, col_i)
            type_coords[val].add((row_i, col_i))

    del type_coords['.']

    return type_coords


def find_pairs(type_coords):
    pairs = defaultdict(list)
    for type, coords in type_coords.items():
        coords = list(coords)
        for i in range(len(coords) - 1):
            coord1 = coords[i]
            for j in range(i + 1, len(coords)):
                coord2 = coords[j]
                pairs[type].append((coord1, coord2))
    return pairs


# calculate distance between each pair
def calculate_distance_between_pairs(grid, pairs):
    HEIGHT, WIDTH = len(grid), len(grid[0])

    results = set()
    for type, type_pairs in pairs.items():
        for (x1, y1), (x2, y2) in type_pairs:
            xd, yd = x1 - x2, y1 - y2

            nx1, ny1 = x1 + xd, y1 + yd
            while 0 <= nx1 < HEIGHT and 0 <= ny1 < WIDTH:
                results.add((type, nx1, ny1))
                nx1, ny1 = nx1 + xd, ny1 + yd

            nx2, ny2 = x2 - xd, y2 - yd
            while 0 <= nx2 < HEIGHT and 0 <= ny2 < WIDTH:
                results.add((type, nx2, ny2))
                nx2, ny2 = nx2 - xd, ny2 - yd

    return results
        

def truncate_oob(grid, results):
    results2 = set()
    for type, row, col in results:
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            continue

        grid[row][col] = '#'
        results2.add((row, col))

    return results2


def debug_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            val = grid[row][col]
            print(val, end='')
        print()


def run():
    grid = read_input()
    type_coords = find_coordinates(grid)
    pairs = find_pairs(type_coords)
    results = calculate_distance_between_pairs(grid, pairs)
    results = truncate_oob(grid, results)
    debug_grid(grid)

    flat = [x for y in grid for x in y]
    nodes = [x for x in flat if x != '#' and x != '.']

    print(f'Part 2: {len(results) + len(nodes)}')


if __name__ == '__main__':
    run()

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