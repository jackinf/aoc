from collections import defaultdict


def draw_grid(bkeys, bpos, RC, special_mode=False):
    ROWS, COLS = RC
    ids = bpos.keys()

    blizzards = defaultdict(list)
    for id in ids:
        row, col = bpos[id]
        blizzards[(row, col)].append(id)

    output = '\n'
    output += '# ' + '#' * COLS
    output += '\n'

    for row in range(ROWS):
        output += '#'
        for col in range(COLS):
            ids = blizzards.get((row, col), [])

            if len(ids) == 0:
                symbol = '.'
            elif len(ids) == 1:
                symbol = bkeys[ids[0]]
            else:
                symbol = str(len(ids))

            if special_mode:
                symbol = '.' if symbol == '.' else ' '

            output += symbol
        output += '#'
        output += '\n'

    output += '#' * COLS + ' #'
    output += '\n'

    if special_mode:
        time.sleep(0.5)
        print('\r' + output, flush=True)
    else:
        print(output)
