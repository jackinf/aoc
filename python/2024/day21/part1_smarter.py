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
def get_cost_from_keypad(code: str, depth: int) -> int:
    print()
    print(f'Code: {code}, Depth: {depth}')
    prev = 'A'

    acc_cost = 0
    for curr in code:
        paths = navigate_pad(xy_key(prev), xy_key(curr), is_numpad=False)

        best_cost = float('inf')
        best_path = ''
        for path in paths:
            if depth == 0:
                cost = calculate_base_cost(path)
            else:
                cost = get_cost_from_keypad(path, depth - 1)

            if cost < best_cost:
                best_cost = cost
                best_path = path

        # print(f'Best path: {best_path}. Best cost: {best_cost}')
        acc_cost += best_cost
        prev = curr

    return acc_cost


@cache
def get_pad_presses(code: str, is_numpad: bool = True) -> str:
    prev_code = 'A'

    best_path = ''
    best_cost = float('inf')
    for curr in code:
        source = xy(prev_code, is_numpad)
        target = xy(curr, is_numpad)
        paths = navigate_pad(source, target, is_numpad)

        for path in paths:
            cost = get_cost_from_keypad(path, 1)
            if cost < best_cost:
                best_cost = cost
                best_path = path
        # paths = collect_paths(combined_paths, paths)
        # combined_paths.append(paths)

        prev_code = curr

    return best_path


def run():
    lines = read_input('sample2.txt')

    final_result = 0
    for code in lines:
        code3 = get_pad_presses(code, True)
        # code2 = get_pad_presses(code1, True)
        # code3 = get_pad_presses(code2, True)

        print(f'{code}: {len(code3)} * {int(code[:-1])}')
        result = len(code3) * int(code[:-1])
        final_result += result

    print(f'Part 1: {final_result}')


def experiment():
    cost1 = calculate_base_cost('v<<A')
    cost2 = calculate_base_cost('>^>A')
    print(cost1, cost2)

    cost3 = get_cost_from_keypad('^', depth=1)
    print(cost3)


if __name__ == '__main__':
    # run()
    experiment()


