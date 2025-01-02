from functools import cache
from typing import Dict, Tuple, Set


def read_input(file_name: str):
    with open(file_name) as f:
        return f.read().split('\n')

def create_graph(pad: Dict[str, Tuple[int, int]], skip: Tuple[int, int]):
    graph = {}

    for i1, (r1, c1) in pad.items():
        for i2, (r2, c2) in pad.items():
            p1 = '<' * (c1 - c2)
            p2 = 'v' * (r2 - r1)
            p3 = '^' * (r1 - r2)
            p4 = '>' * (c2 - c1)
            path = p1 + p2 + p3 + p4

            # if we cross the cell that we have to skip, then we just take a route that's a reflection
            if skip == (r1, c2) or skip == (r2, c1):
                path = path[::-1]

            graph[(i1, i2)] = path + "A"

    return graph

def run():
    lines = read_input('input.txt')

    numpad = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
                     '0': (3, 1), 'A': (3, 2)
    }

    dirpad = {
                     '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2),
    }

    numpad_graph = create_graph(numpad, (3, 0))
    dirpad_graph = create_graph(dirpad, (0, 0))

    print(numpad_graph)
    print(dirpad_graph)

    @cache
    def solve(code: str, depth: int, is_numpad: bool) -> int:
        if depth == 0:
            return len(code)

        prev = 'A'
        graph = numpad_graph if is_numpad else dirpad_graph
        result = 0
        for char in code:
            next_code = graph[(prev, char)]
            result += solve(next_code, depth - 1, is_numpad=False)
            prev = char

        return result

    final_result = 0
    for code in lines:
        length = solve(code, 26, is_numpad=True)
        final_result += int(code[:-1]) * length

    print(f'Part 2: {final_result}')


if __name__ == '__main__':
    run()