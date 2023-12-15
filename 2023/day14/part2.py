with open('sample.txt', 'r') as f:
    grid = [list(line) for line in f.read().split('\n')]


def calculate(grid):
    results = []
    scores = []
    for col in range(len(grid[0])):
        results.append([])
        scores.append([])

        power = len(grid)
        row_counter = 0
        for row in range(len(grid)):
            if grid[row][col] == 'O':
                results[-1].append((row_counter, 'O'))
                row_counter += 1

                scores[-1].append(power)
                power -= 1
            if grid[row][col] == '#':
                results[-1].append((row, '#'))
                row_counter = row + 1

                power = len(grid) - row - 1
    return results, scores


def construct_grid2(grid, results):
    grid2 = [['.' for _ in row] for row in grid]

    for col, col_arr in enumerate(results):
        for row, symbol in col_arr:
            grid2[row][col] = symbol

    return grid2


def get_total_score(scores):
    return sum([sum(values) for values in scores])


def get_results_key(i, results):
    flat = [x for y in results for x in y]
    results_key = ''.join([f'{a}{b}|' for a,b in flat])
    return results_key
    # return f'{i}-{results_key}'


def debug(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end="")
        print()
    print()


seen = {}
cycle = 1
found = False
cycle_start = -1
cycle_length = -1
MAX = 1_000_000_000
# MAX = 3
while cycle <= MAX:
    for i in ('N', 'W', 'S', 'E'):
        results, scores = calculate(grid)

        if not found:
            key = get_results_key(i, results)
            if key in seen:
                cycle_start = seen[key]
                cycle_length = cycle - seen[key]
                print(f'found a cycle! current count={cycle}, length={cycle_length}, previous at={cycle_start}')
                print(cycle, cycle_start, cycle_length)
                cycle = ((MAX - cycle_start) // cycle_length * cycle_length) + cycle_start
                found = True
            seen[key] = cycle

        grid = construct_grid2(grid, results)
        # grid = list(zip(*grid))[::-1]  # 90 deg counter-clockwise
        grid = list(zip(*grid[::-1]))  # 90 deg clockwise

    cycle += 1

results, scores = calculate(grid)
grid = construct_grid2(grid, results)
debug(grid)

# wrong solution
print(f'Part 2: {get_total_score(scores)}')

# 109449 - too high