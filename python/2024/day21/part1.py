from functools import cache
from typing import List, Tuple

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


@cache
def base_cost(src: str, dest: str) -> int:
    match (src, dest):
        case ('<', 'A'): return 3
        case ('<', '^'): return 2
        case ('<', '>'): return 2
        case ('<', 'v'): return 1
        case ('<', '<'): return 0

        case ('A', '^'): return 1
        case ('A', 'v'): return 2
        case ('A', '<'): return 3
        case ('A', '>'): return 1
        case ('A', 'A'): return 0

        case ('^', '^'): return 0
        case ('^', 'v'): return 1
        case ('^', '<'): return 2
        case ('^', '>'): return 2
        case ('^', 'A'): return 1

        case ('v', '^'): return 1
        case ('v', 'v'): return 0
        case ('v', '<'): return 1
        case ('v', '>'): return 1
        case ('v', 'A'): return 2

        case ('>', '^'): return 2
        case ('>', 'v'): return 1
        case ('>', '<'): return 2
        case ('>', '>'): return 0
        case ('>', 'A'): return 1


@cache
def xy(symbol, is_numpad: bool = True):
    pad = numpad if is_numpad else keypad
    for y in range(len(pad)):
        for x in range(len(pad[0])):
            if pad[y][x] == symbol:
                return x, y
    raise Exception('not found')

@cache
def xy_key(symbol):
    return xy(symbol, is_numpad=False)

@cache
def xy_num(symbol):
    return xy(symbol, is_numpad=True)


def dir_to_arrows(x: int, y: int):
    hor, ver = '', ''

    if x > 0: hor += '>' * x
    elif x < 0: hor += '<' * abs(x)

    if y > 0: ver += 'v' * y
    elif y < 0: ver += '^' * abs(y)

    return hor + ver


@cache
def navigate_pad(start, end, is_numpad: bool = True) -> List[str]:
    x1, y1 = start
    x2, y2 = end
    pad = numpad if is_numpad else keypad

    q = [(x1, y1, '', 5)]
    results = []

    while q:
        x, y, path, left = q.pop(0)

        if x == x2 and y == y2:
            results.append(path + "A")
            continue

        if left <= 0:
            continue

        for dx, dy in ((0, -1), (0, +1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(pad) and 0 <= nx < len(pad[0]) and pad[y][x] != ' ':
                path_delta = dir_to_arrows(dx, dy)
                q.append((nx, ny, path + path_delta, left - 1))

    sorted_results = sorted(results, key=lambda x: len(x))
    min_len = len(sorted_results[0])

    return [result for result in sorted_results if len(result) == min_len]


def read_input(file_name: str):
    with open(file_name) as f:
        return f.read().split('\n')

def collect_paths(paths1: List[str], paths2: List[str]):
    if len(paths1) == 0:
        return paths2

    return [path1 + path2 for path1 in paths1 for path2 in paths2]


@cache
def calculate_base_cost(path):
    total_cost = 0
    path2 = 'A' + path
    for i in range(1, len(path2)):
        cost = base_cost(path2[i - 1], path2[i])
        total_cost += cost
    return total_cost


@cache
def get_cost_from_pad(code: str, depth: int, is_numpad=False) -> Tuple[int, str]:
    print()
    print(f'Code: {code}, Depth: {depth}')
    prev = 'A'

    acc_cost = 0
    full_best_path = ''
    for curr in code:
        src = xy(prev, is_numpad=is_numpad)
        dest = xy(curr, is_numpad=is_numpad)
        paths = navigate_pad(src, dest, is_numpad=is_numpad)

        best_cost = float('inf')
        best_path = ''
        for path in paths:
            if depth == 0:
                cost = calculate_base_cost(path)
            else:
                cost, path = get_cost_from_pad(path, depth - 1, is_numpad=False)  # every depth down is now keypad

            if cost < best_cost:
                best_cost = cost
                best_path = path

        print(f'Code: {code}, Depth: {depth}. Best path: {best_path}. Best cost: {best_cost}')
        acc_cost += best_cost
        prev = curr
        full_best_path += best_path

    return acc_cost, full_best_path


def run():
    lines = read_input('input.txt')

    final_result = 0
    for code in lines:
        cost, path = get_cost_from_pad(code, depth=2, is_numpad=True)

        print(f'{code}: {len(path)} * {int(code[:-1])}')
        result = len(path) * int(code[:-1])
        final_result += result

    print(f'Part 1: {final_result}')


def experiment():
    # cost1 = calculate_base_cost('v<<A')
    # cost2 = calculate_base_cost('>^>A')
    # print(cost1, cost2)
    #
    # res3 = get_cost_from_pad('^', depth=1)
    # print(res3)
    #
    # res4 = get_cost_from_pad('^<A', depth=1)
    # print(res4)

    cost51, path1 = get_cost_from_pad('029A', depth=2, is_numpad=True)
    cost52, path2 = get_cost_from_pad('980A', depth=2, is_numpad=True)
    cost53, path3 = get_cost_from_pad('179A', depth=2, is_numpad=True)
    cost54, path4 = get_cost_from_pad('456A', depth=2, is_numpad=True)
    cost55, path5 = get_cost_from_pad('379A', depth=2, is_numpad=True)
    print(cost51, len(path1))
    print(cost52, len(path2))
    print(cost53, len(path3))
    print(cost54, len(path4))
    print(cost55, len(path5))


if __name__ == '__main__':
    run()
    # experiment()


