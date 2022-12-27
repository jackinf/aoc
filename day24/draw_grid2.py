from typing import Dict, Tuple, Set


def draw_grid2(RC, bpos_rev: Dict[Tuple[int, int], Set[str]], step, clean_mode=False):
    ROWS, COLS = RC

    output = f'\nStep: {step}\n'
    output += '# ' + '#' * COLS
    output += '\n'

    for row in range(ROWS):
        output += '#'
        for col in range(COLS):
            keys = set()

            if "<" in bpos_rev.get((row, (col + step) % COLS), set()):
                keys.add("<")
            if ">" in bpos_rev.get((row, (col - step) % COLS), set()):
                keys.add(">")
            if "^" in bpos_rev.get(((row + step) % ROWS, col), set()):
                keys.add("^")
            if "v" in bpos_rev.get(((row - step) % ROWS, col), set()):
                keys.add("v")

            if len(keys) == 0:
                symbol = '.'
            elif len(keys) == 1:
                symbol = keys.pop()
            else:
                symbol = str(len(keys))

            if clean_mode:
                symbol = '.' if symbol == '.' else ' '

            output += symbol
        output += '#'
        output += '\n'

    output += '#' * COLS + ' #'
    output += '\n'

    print(output)
