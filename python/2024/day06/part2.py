from typing import Tuple, Set
from itertools import cycle

WALL = '#'
EMPTY = '.'
PLAYER = '^'
LIMIT = 1000
N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)
directions = [N, E, S, W]


def read_input():
    with open('input.txt') as f:
        lines = f.read().split('\n')
        grid = [list(x) for x in lines]

    start = next((y, x) for y, row in enumerate(grid) for x, val in enumerate(row) if val == PLAYER)
    grid[start[0]][start[1]] = EMPTY

    return grid, start


def debug_grid(grid, blocks):
    """Print the grid with successful enclosures marked."""

    print()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in blocks:
                print('O', end='')
            else:
                print(grid[row][col], end='')
        print()
    print('====')
    print()


def check_if_loop(grid, dir_index_: int, curr: Tuple[int, int]):
    dir_index = (dir_index_ + 1) % len(directions)
    seen = set()
    seen.add(curr)

    while True:
        delta = directions[dir_index]
        nei_row, nei_col = tuple(map(sum, zip(curr, delta)))

        # if we manage to exit the grid, then we're not in the loop
        if not (0 <= nei_row < len(grid) and 0 <= nei_col < len(grid[0])):
            return False  # we are NOT in the loop

        # have we already entered this cell (from this direction) before?
        seen_key = (nei_row, nei_col, delta)
        if seen_key in seen:
            return True  # we are in the loop
        seen.add(seen_key)

        if grid[nei_row][nei_col] == WALL:
            dir_index = (dir_index + 1) % len(directions)
            continue

        if grid[nei_row][nei_col] == EMPTY:

            curr = nei_row, nei_col
            continue

        raise Exception('should not get here')


def walk_till_exit(grid, curr: Tuple[int, int]):
    dir_index = 0
    blocks = set()

    while True:
        delta = directions[dir_index]
        nei_row, nei_col = tuple(map(sum, zip(curr, delta)))

        # finish - we exit the grid
        if not (0 <= nei_row < len(grid) and 0 <= nei_col < len(grid[0])):
            return blocks

        # turn, if we hit the wall
        if grid[nei_row][nei_col] == WALL:
            dir_index = (dir_index + 1) % len(directions)
            continue

        # we can walk here
        if grid[nei_row][nei_col] == EMPTY:

            # let's test if we are in the loop by putting a wall in front of us
            grid[nei_row][nei_col] = WALL  # set the wall
            if check_if_loop(grid, dir_index, curr):
                blocks.add((nei_row, nei_col))
            grid[nei_row][nei_col] = EMPTY  # revert

            curr = nei_row, nei_col
            continue

        raise Exception('should not get here')


def run():
    grid, start = read_input()
    blocks: Set[Tuple[int, int]] = walk_till_exit(grid, start)

    if start in blocks:
        blocks.remove(start)

    debug_grid(grid, blocks)
    print(f'Part 2: {len(blocks)}')


run()
# 2657 - wrong
# 1914 - wrong
# 1781 - wrong
# 1780 - wrong
# 1771 - wrong

