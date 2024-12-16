import heapq
from collections import defaultdict

EAST = (0, 1)
WEST = (0, -1)
NORTH = (-1, 0)
SOUTH = (1, 0)

DIRS = [EAST, SOUTH, WEST, NORTH]

WALL = '#'
EMPTY = '.'

STEP_COST = 1
TURN_COST = 1000


def read_input():
    with open('input.txt') as f:
        lines = f.read().split('\n')

    return [list(x) for x in lines]


def get_symbol(grid, symbol):
    return next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == symbol)


def heuristic(curr_row, curr_col, end_row, end_col):
    return abs(curr_row - end_row) + abs(curr_col - end_col)


def traverse_grid(grid):
    start_row, start_col = get_symbol(grid, 'S')
    end_row, end_col = get_symbol(grid, 'E')

    q = [(0, 0, start_row, start_col)]  # score, dir, start_row, start_col
    seen = set()
    costs = defaultdict(lambda: float('inf'))
    costs[(start_row, start_col)] = 0

    while q:
        score, dir_index, curr_row, curr_col = heapq.heappop(q)

        # optional cache check; not required in tight maze
        cache_key = (curr_row, curr_col)
        if cache_key in seen:
            continue
        seen.add(cache_key)

        if curr_row == end_row and curr_col == end_col:
            return costs[(curr_row, curr_col)]

        for delta, turn_cost in [(0, 0), (-1, TURN_COST), (1, TURN_COST)]:
            new_dir_index = (dir_index + delta) % len(DIRS)
            row_delta, col_delta = DIRS[new_dir_index]
            next_row, next_col = curr_row + row_delta, curr_col + col_delta

            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != WALL:
                new_cost = costs[(curr_row, curr_col)] + STEP_COST + turn_cost
                if new_cost < costs[(next_row, next_col)]:
                    costs[(next_row, next_col)] = new_cost
                    h = heuristic(next_row, next_col, end_row, end_col)
                    heapq.heappush(q, (new_cost + h, new_dir_index, next_row, next_col))

    return -1


def run():
    grid = read_input()
    min_score = traverse_grid(grid)

    print(f'Part 1: {min_score}')


if __name__ == '__main__':
    run()