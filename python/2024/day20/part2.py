from collections import defaultdict, Counter

WALL = '#'
EMPTY = '.'
STEP_COST = 1
START = 'S'
END = 'E'

def count_walls(grid):
    wall_count = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == WALL:
                wall_count += 1
    return wall_count

def find_symbol(grid, symbol):
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == symbol:
                return row, col
    raise Exception('not found')

def read_input():
    with open('sample1.txt') as f:
        return [list(line) for line in f.read().split('\n')]

def oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def traverse(grid, start, end, cut_limit: int):
    q = [(0, start, set())]

    seen = set()

    results = []
    while q:
        steps, curr, cuts = q.pop(0)
        row, col = curr

        cache_key = tuple(cuts) + (curr,)
        if cache_key in seen:
            continue
        seen.add(cache_key)

        if curr == end:
            results.append(steps)
            continue

        for nei in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
            nrow, ncol = nei

            if oob(grid, nrow, ncol):
                continue

            if grid[nrow][ncol] == EMPTY:
                q.append((steps + STEP_COST, nei, cuts))
                continue

            if grid[nrow][ncol] == WALL:
                if len(cuts) == cut_limit:
                    continue

                if (nrow, ncol) in cuts:
                    continue

                cuts2 = set(cuts)
                cuts2.add((nrow, ncol))
                q.append((steps + STEP_COST, nei, cuts2))

    return results

def analyze_counter(counter, normal_score):
    for k, v in sorted(counter.items(), key=lambda x: x[0], reverse=True):
        saved = normal_score - k
        print(f'There are {v} cheats that save {saved} picoseconds.')


def debug_grid(grid, marks):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in marks:
                print('O', end='')
            else:
                print('.' if grid[row][col] == WALL else ' ', end='')
        print()

def run():
    grid = read_input()
    print(f'Grid size M x N: {len(grid) * len(grid[0])}')

    start = find_symbol(grid, START)
    grid[start[0]][start[1]] = EMPTY
    end = find_symbol(grid, END)
    grid[end[0]][end[1]] = EMPTY

    normal_results = traverse(grid, start, end, 0)
    print(f'normal_results: {normal_results}')

    # no idea... i realized that as the maze is narrow, then there's no need for a-star
    # however now i don't know how find so many combinations

    cheat_score = traverse(grid, start, end, 1)
    print(f'cheat_score: {cheat_score}')

run()
