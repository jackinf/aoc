from pprint import pprint

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


def get_results_key(results):
    flat = [x for y in results for x in y]
    return ''.join([f'{a}{b}' for a,b in flat])


def debug(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end="")
        print()
    print()


seen = {}
# while True:
for i in range(4):
    results, scores = calculate(grid)
    print(results, get_results_key(results))
    # TODO: calculate cache from results, map cached results to score & i
    # print(get_total_score(scores))
    grid = construct_grid2(grid, results)
    grid = list(zip(*grid[::-1]))

    # print(f'After {cycle + 1} cycle:')
    # debug(grid)

# total = sum([sum(values) for values in results])
# print(f'Part 1: {total}')
