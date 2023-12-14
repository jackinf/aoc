from pprint import pprint

with open('input.txt', 'r') as f:
    grid = [list(line) for line in f.read().split('\n')]

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

total = sum([sum(values) for values in results])
print(f'Part 1: {total}')
