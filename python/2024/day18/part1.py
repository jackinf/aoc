import heapq
from collections import defaultdict

# WIDTH = 6 + 1
# HEIGHT = 6 + 1
# LIMIT = 12
WIDTH = 70 + 1
HEIGHT = 70 + 1
LIMIT = 1024

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
STEP_COST = 1

WALL = '#'
EMPTY = '.'


def read_input():
    with open('input.txt') as f:
        lines = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in f.read().split('\n')]
        return lines


def debug_grid(grid, coords):
    coords_set = set(coords[:LIMIT])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (col, row) in coords_set:
                print(WALL, end='')
            else:
                print(EMPTY, end='')
        print()


def heuristic(row, col, end_row, end_col):
    return abs(row - end_row) + abs(col - end_col)


def a_star(coords):
    coords_set = set(coords[:LIMIT])

    q = [(-1, 0, 0, 1)]  # score row, col, steps
    end_row, end_col = HEIGHT - 1, WIDTH - 1
    seen = set()
    costs = defaultdict(lambda: float('inf'))
    costs[(0, 0)] = 0

    while q:
        score, row, col, steps = heapq.heappop(q)

        # out of bounds check
        if not (0 <= row < HEIGHT and 0 <= col < WIDTH):
            continue

        # is it a corrupt memory (a wall)
        if (col, row) in coords_set:
            continue

        # did we make it to the finish
        if row == end_row and col == end_col:
            return steps - 1

        if (row, col) in seen:
            continue
        seen.add((row, col))

        for drow, dcol in (NORTH, SOUTH, EAST, WEST):
            nrow, ncol = row + drow, col + dcol

            new_cost = costs[(row, col)] + STEP_COST
            if new_cost < costs[(nrow, ncol)]:
                costs[(nrow, ncol)] = new_cost
                h = heuristic(nrow, ncol, end_row, end_col)
                heapq.heappush(q, (new_cost + h, nrow, ncol, steps + 1))

    return -1


def run():
    coords = read_input()
    print(coords)

    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    debug_grid(grid, coords)

    steps = a_star(coords)
    print(steps)


run()