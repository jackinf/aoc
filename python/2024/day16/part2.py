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
    with open('sample1.txt') as f:
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
    costs = defaultdict(lambda: float('inf'))
    costs[(start_row, start_col)] = 0

    parents = {(start_row, start_col): None}
    paths = []

    while q:
        score, dir_index, curr_row, curr_col = heapq.heappop(q)

        if curr_row == end_row and curr_col == end_col:
            path = []
            while parents[(curr_row, curr_col)] is not None:
                path.append((curr_row, curr_col))
                curr_row, curr_col = parents[(curr_row, curr_col)]
            path.reverse()
            paths.append(path)
            continue

        for delta, turn_cost in [(0, 0), (-1, TURN_COST), (1, TURN_COST)]:
            new_dir_index = (dir_index + delta) % len(DIRS)
            row_delta, col_delta = DIRS[new_dir_index]
            next_row, next_col = curr_row + row_delta, curr_col + col_delta

            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != WALL:
                new_cost = costs[(curr_row, curr_col)] + STEP_COST + turn_cost
                if new_cost < costs[(next_row, next_col)]:
                    costs[(next_row, next_col)] = new_cost
                    h = heuristic(next_row, next_col, end_row, end_col)
                    parents[(next_row, next_col)] = (curr_row, curr_col)
                    heapq.heappush(q, (new_cost + h, new_dir_index, next_row, next_col))

    return paths


def run():
    grid = read_input()
    paths = traverse_grid(grid)

    cells = set()
    for path in paths:
        for cell in path:
            cells.add(cell)

    print(f'Part 2: {len(cells)}')


if __name__ == '__main__':
    run()