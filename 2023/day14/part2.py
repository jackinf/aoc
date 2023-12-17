from collections import defaultdict
from pprint import pprint

with open('sample.txt', 'r') as f:
    grid = [list(line) for line in f.read().split('\n')]


def calculate_north_load(grid):
    results = []
    for col in range(len(grid[0])):
        results.append([])

        power = len(grid)
        for row in range(len(grid)):
            if grid[row][col] == 'O':
                results[-1].append(power)
                power -= 1
            if grid[row][col] == '#':
                power = len(grid) - row - 1

    return sum([sum(values) for values in results])


seen = defaultdict(set)
for cycle in range(1_000_000_000):
    # flip
    grid = list(zip(*grid[::-1]))

    total = calculate_north_load(grid)
    if total in seen[cycle % 4]:
        print(f'found a cycle at {cycle}')
        break
    seen[cycle % 4].add(total)


# total = calculate_north_load(grid)
# print(f'Part 2: {total}')
