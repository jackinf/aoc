from collections import Counter
from functools import reduce
from pprint import pprint
from typing import Tuple, List


DEBUG = False
WIDTH = 101  # width
HEIGHT = 103  # height
MAX_SECONDS = 100
# WIDTH = 11  # width
# HEIGHT = 7  # height
# MAX_SECONDS = 100

type ROBOT = Tuple[int, int, int, int]
type ROBOTS = List[ROBOT]
type Q4_SAFETY = List[int]


def read_input() -> ROBOTS:
    with open('input.txt') as f:
        lines = f.read().split('\n')

    robots = []
    for line in lines:
        left, right = line.split()
        col, row = [int(val) for val in left[2:].split(',')]
        col_delta, row_delta = [int(val) for val in right[2:].split(',')]

        robots.append((col, row, col_delta, row_delta))

    return robots


def pr(output = None, *args, **kwargs):
    if DEBUG:
        if not output:
            print()
        else:
            print(output, *args, **kwargs)


def step(state1: ROBOTS) -> ROBOTS:
    state2: ROBOTS = []
    for col, row, col_delta, row_delta in state1:
        col += col_delta
        col %= WIDTH
        row += row_delta
        row %= HEIGHT
        state2.append((col, row, col_delta, row_delta))
    return state2


def calculate_safety_factor(state: ROBOTS) -> Q4_SAFETY:
    qs: Q4_SAFETY = [0, 0, 0, 0]
    W2, H2 = WIDTH // 2, HEIGHT // 2

    for col, row, _, _ in state:
        if col < W2 and row < H2:
            qs[0] += 1
        if col > W2 and row < H2:
            qs[1] += 1
        if col < W2 and row > H2:
            qs[2] += 1
        if col > W2 and row > H2:
            qs[3] += 1

    return qs


def debug_grid(state: ROBOTS):
    counter = Counter([(px, py) for px, py, vx, vy in state])

    for row in range(HEIGHT):
        for col in range(WIDTH):
            val = counter[(col, row)]
            val = '.' if val == 0 else str(val)
            print(val, end='')
        print()


def run():
    robots = read_input()
    pprint(robots)

    for second in range(MAX_SECONDS):
        if second == 0:
            pr('Initial state:')
        else:
            pr(f'After {second} seconds:')

        # debug_grid(robots)
        robots = step(robots)

        pr()

    quarter_safety = calculate_safety_factor(robots)
    final_result = reduce(lambda x, y: x * y, quarter_safety)

    pr(robots)
    pr(quarter_safety)
    debug_grid(robots)

    print(f'Part 1: {final_result}')


run()