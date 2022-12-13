import collections.abc
from typing import Union, List


def is_arr(x):
    return isinstance(x, collections.abc.Sequence)

def parse_arr(line: str):
    return eval(line)  # I'm cheating here :) TODO: implement parsing


def compare_pairs(left: Union[int, List], right: Union[int, List]) -> int:
    """
    :return: 1 -> in order, 0 -> equal, -1, not in order
    """

    if is_arr(left) and not is_arr(right):
        return compare_pairs(left, [right])

    if not is_arr(left) and is_arr(right):
        return compare_pairs([left], right)

    if is_arr(left) and is_arr(right):
        i = 0
        while True:
            if i >= len(left) and i >= len(right): return 0
            if i >= len(left) and i < len(right): return 1
            if i < len(left) and i >= len(right): return -1

            result = compare_pairs(left[i], right[i])
            if result != 0:
                return result
            i += 1

    if not is_arr(left) and not is_arr(right):
        return 0 if left == right else 1 if left < right else -1

    raise Exception('should not make it here')


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    parsed_lines = []
    for line in lines:
        if not line: continue
        parsed_lines.append(parse_arr(line))

    part1_result = 0
    for i in range(0, len(parsed_lines), 2):
        left = parsed_lines[i]
        right = parsed_lines[i+1]
        if compare_pairs(left, right) == 1:
            part1_result += (i//2)+1

    print(f'Result 1: {part1_result}')

    parsed_lines.extend([[[2]], [[6]]])

    # Bubble sort
    for i in range(len(parsed_lines)):
        for j in range(len(parsed_lines)):
            if compare_pairs(parsed_lines[i], parsed_lines[j]) == -1:
                parsed_lines[i], parsed_lines[j] = parsed_lines[j], parsed_lines[i]
    parsed_lines.reverse()
    x = parsed_lines.index([[2]]) + 1
    y = parsed_lines.index([[6]]) + 1

    print(f'Result 2: {x * y}')
