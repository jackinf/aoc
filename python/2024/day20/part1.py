import heapq
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

def heuristic(row, col, end_row, end_col):
    return abs(row - end_row) + abs(col - end_col)

def oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def a_star(grid, start, end):
    costs = defaultdict(lambda: float('inf'))
    costs[start] = 0
    q = [(0, start)]

    seen = set()

    while q:
        steps, curr = heapq.heappop(q)

        if curr in seen:
            continue
        seen.add(curr)

        # if grid[curr[0]][curr[1]] == WALL:
        #     continue

        if curr == end:
            return costs[curr]

        for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nrow, ncol = curr[0] + drow, curr[1] + dcol
            new_cost = costs[curr] + STEP_COST
            if not oob(grid, nrow, ncol) and new_cost < costs[(nrow, ncol)] and grid[nrow][ncol] != WALL:
                costs[(nrow, ncol)] = new_cost
                h = heuristic(nrow, ncol, end[0], end[1])
                heapq.heappush(q, (new_cost + h, (nrow, ncol)))

def analyze_counter(counter, normal_score):
    for k, v in sorted(counter.items(), key=lambda x: x[0], reverse=True):
        saved = normal_score - k
        print(f'There are {v // 2} cheats that save {saved} picoseconds.')

def run():
    grid = read_input()
    print(grid, len(grid) * len(grid[0]))

    start = find_symbol(grid, START)
    grid[start[0]][start[1]] = EMPTY
    end = find_symbol(grid, END)
    grid[end[0]][end[1]] = EMPTY

    total_wall_count = count_walls(grid)
    walls_analyzed = 0

    normal_score = a_star(grid, start, end)
    threshold = normal_score - 100
    print(f'Normal score: {normal_score}')

    cheats_100ps_or_more = 0
    counter = Counter()
    seen = {}
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == WALL:
                walls_analyzed += 1
                print(f'Walls analyzed: {walls_analyzed} out of {total_wall_count}')

                grid[row][col] = EMPTY

                # try out 4 combinations by removing 2nd wall
                for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nrow, ncol = row + drow, col + dcol
                    if grid[nrow][ncol] == WALL:
                        grid[nrow][ncol] = EMPTY
                        score = a_star(grid, start, end)
                        counter[score] += 1
                        if score <= threshold:
                            cheats_100ps_or_more += 1
                        grid[nrow][ncol] = WALL

                grid[row][col] = WALL

    analyze_counter(counter, normal_score)

    print(f'Part 1: {cheats_100ps_or_more}')

run()

# 4808 - too high