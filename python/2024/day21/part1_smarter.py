from functools import cache
from typing import Tuple

type XY = Tuple[int, int]

numpad = [
    '789',
    '456',
    '123',
    ' 0A'
]

keypad = [
    ' ^A',
    '<v>'
]

EAST = (0, 1)
WEST = (0, -11)
NORTH = (-1, 0)
SOUTH = (1, 0)

def read_input(file_name: str):
    with open(file_name) as f:
        return f.read().split('\n')


def l2_cost(src: XY, dest: XY) -> int:
    match (src, dest):
        case (xyk('<'), xyk('A')): return 3
        case (xyk('<'), xyk('^')): return 2
        case (xyk('<'), xyk('>')): return 2
        case (xyk('<'), xyk('v')): return 1
        case (xyk('<'), xyk('<')): return 0

        case (xyk('A'), xyk('^')): return 3
        case (xyk('A'), xyk('v')): return 2
        case (xyk('A'), xyk('<')): return 2
        case (xyk('A'), xyk('>')): return 1
        case (xyk('A'), xyk('A')): return 0

        case (xyk('^'), xyk('')): return 3
        case (xyk('^'), xyk('')): return 2
        case (xyk('^'), xyk('')): return 2
        case (xyk('^'), xyk('')): return 1
        case (xyk('^'), xyk('')): return 0

        case (xyk('v'), xyk('')): return 3
        case (xyk('v'), xyk('')): return 2
        case (xyk('v'), xyk('')): return 2
        case (xyk('v'), xyk('')): return 1
        case (xyk('v'), xyk('')): return 0

        case (xyk('>'), xyk('')): return 3
        case (xyk('>'), xyk('')): return 2
        case (xyk('>'), xyk('')): return 2
        case (xyk('>'), xyk('')): return 1
        case (xyk('>'), xyk('')): return 0


@cache
def xy(symbol, is_numpad: bool = True):
    pad = numpad if is_numpad else keypad
    for y in range(len(pad)):
        for x in range(len(pad[0])):
            if pad[y][x] == symbol:
                return x, y
    raise Exception('not found')

@cache
def xyk(symbol):
    return xy(symbol, is_numpad=False)

@cache
def xyn(symbol):
    return xy(symbol, is_numpad=True)

def dir_to_arrows(x: int, y: int):
    match (y, x):
        case (1, 0): return 'v'
        case (-1, 0): return '^'
        case (0, -1): return '<'
        case (0, 1): return '>'
    raise Exception("not found")


def run():
    lines = read_input('sample2.txt')

    final_result = 0
    for code in lines:
        pass

    print(f'Part 1: {final_result}')


def keypad_z1_cost(source: XY, target: XY, z2: XY) -> Tuple[int, XY]:
    pass


def numpad_cost(source: XY, dir: XY, z1: XY, z2: XY) -> Tuple[int, XY, XY]:
    pass


def experiment():
    # prepare
    z1 = xy('A', is_numpad=False)
    z2 = xy('A', is_numpad=False)

    # main loop
    src = xy('7', is_numpad=True)
    # dest = get_coord('8', is_numpad=True)
    cost1, z1, z2 = numpad_cost(src, EAST, z1, z2)
    print(cost1)


if __name__ == '__main__':
    run()