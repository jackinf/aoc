from collections import defaultdict
from pprint import pprint


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


def draw_grid(bkeys, bpos, RC):
    ROWS, COLS = RC
    ids = bpos.keys()

    blizzards = defaultdict(list)
    for id in ids:
        row, col = bpos[id]
        blizzards[(row, col)].append(id)

    print()
    print('# ', end='')
    print('#' * ROWS, end='')
    print()

    for row in range(ROWS):
        print('#', end='')
        for col in range(COLS):
            ids = blizzards.get((row, col), [])

            if len(ids) == 0:
                symbol = '.'
            elif len(ids) == 1:
                symbol = bkeys[ids[0]]
            else:
                symbol = str(len(ids))

            print(symbol, end='')
        print('#', end='')
        print()

    print('#' * ROWS, end='')
    print(' #', end='')
    print()


if __name__ == '__main__':
    with open('sample1.txt') as f:
        grid = [list(line.strip()) for line in f]
        # cut walls
        grid = [[col for col in row][1:-1] for row in grid][1:-1]
    RC = len(grid), len(grid[0])
    pprint(grid)

    bkeys, bpos = collect_blizzards(grid)
    pprint(bkeys)
    pprint(bpos)

    move_blizzards(bkeys, bpos, RC)
    pprint(bkeys)
    pprint(bpos)

    step = 0
    while step < 10:
        move_blizzards(bkeys, bpos, RC)
        draw_grid(bkeys, bpos, RC)
        step += 1