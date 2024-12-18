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


def reconstruct_all_paths(parent_map, start, end):
    all_paths = []

    def backtrack(node, path):
        if node == start:
            all_paths.append(path[::-1])
            return

        for parent in parent_map.get(node, []):
            backtrack(parent, path + [node])

    backtrack(end, [])
    return all_paths


def traverse_grid(grid):
    start = get_symbol(grid, 'S')
    end = get_symbol(grid, 'E')
    end_row, end_col = end

    q = [(0, 0, start)]  # score, dir, start_row, start_col
    costs = defaultdict(lambda: float('inf'))
    costs[start] = 0
    parent_map = {start: []}

    while q:
        score, dir_index, curr = heapq.heappop(q)

        if curr == end:
            continue

        for delta, turn_cost in [(0, 0), (-1, TURN_COST), (1, TURN_COST)]:
            new_dir_index = (dir_index + delta) % len(DIRS)
            row_delta, col_delta = DIRS[new_dir_index]
            curr_row, curr_col = curr
            next_row, next_col = curr_row + row_delta, curr_col + col_delta
            nei = (next_row, next_col)

            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != WALL:
                new_cost = costs[curr] + STEP_COST + turn_cost

                if new_cost < costs[nei]:
                    costs[nei] = new_cost
                    h = heuristic(next_row, next_col, end_row, end_col)
                    heapq.heappush(q, (new_cost + h, new_dir_index, nei))

                    if nei not in parent_map:
                        parent_map[nei] = []
                    parent_map[nei].append(curr)

    return reconstruct_all_paths(parent_map, start, end)


def debug_grid(grid, paths):
    unique_cells = set([x for y in paths for x in y])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in unique_cells:
                print('O', end='')
            else:
                print(grid[row][col], end='')
        print()


def run():
    grid = read_input()
    paths = traverse_grid(grid)

    print(len(set([x for y in paths for x in y])))
    # print(f'Part 2: {len(set(paths))}')

    debug_grid(grid, paths)


if __name__ == '__main__':
    run()