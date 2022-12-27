import time
from collections import defaultdict
from pprint import pprint

from day24.bfs import bfs
from day24.draw_grid2 import draw_grid2

# Blizzard symbols
SYMBOLS = {'>', '<', '^', 'v'}


def collect_blizzards(grid):
    ROWS, COLS = len(grid), len(grid[0])
    blizzard_key = {}
    blizzard_pos = {}

    next_id = 1
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] in SYMBOLS:
                blizzard_key[next_id] = grid[row][col]
                blizzard_pos[next_id] = (row, col)
                next_id += 1

    return blizzard_key, blizzard_pos

def move_blizzards(bkeys, bpos, RC):
    ROWS, COLS = RC

    for id in bpos.keys():
        key = bkeys[id]
        row, col = bpos[id]

        row += 1 if key == 'v' else -1 if key == '^' else 0
        col += 1 if key == '>' else -1 if key == '<' else 0

        row %= ROWS
        col %= COLS

        bpos[id] = (row, col)


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [list(line.strip()) for line in f]
        # cut walls
        grid = [[col for col in row][1:-1] for row in grid][1:-1]
    RC = len(grid), len(grid[0])
    ROWS, COLS = RC
    pprint(grid)

    bkeys, bpos = collect_blizzards(grid)
    pprint(bkeys)
    pprint(bpos)

    bpos_rev = defaultdict(set)
    for id, (row, col) in bpos.items():
        bpos_rev[(row, col)].add(bkeys[id])

    move_blizzards(bkeys, bpos, RC)
    pprint(bkeys)
    pprint(bpos)

    # step = 0
    # while step < 10:
    #     move_blizzards(bkeys, bpos, RC)
    #     draw_grid(bkeys, bpos, RC, special_mode=True)
    #     step += 1

    print('Demo start.')

    draw_grid2(RC, bpos_rev, 0)
    draw_grid2(RC, bpos_rev, 1)
    draw_grid2(RC, bpos_rev, 2)
    draw_grid2(RC, bpos_rev, 3)

    print('Demo end.')

    bfs(RC, bpos_rev)
