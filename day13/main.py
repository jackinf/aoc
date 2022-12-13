import collections.abc
from typing import Union, List


def is_arr(x):
    return isinstance(x, collections.abc.Sequence)

def parse_arr(line: str):
    return eval(line)  # I'm cheating here :)


def compare_pairs(left: Union[int, List], right: Union[int, List]) -> int:
    """
    :return: 1 -> in order, 0 -> equal, -1, not in order
    """

    if is_arr(left) and not is_arr(right):
        return compare_pairs(left, [right])

    if not is_arr(left) and is_arr(right):
        return compare_pairs([left], right)

    if is_arr(left) and is_arr(right):
        while True:
            if not left and not right: return 0
            if not left and right: return 1
            if left and not right: return -1

            result = compare_pairs(left.pop(0), right.pop(0))
            if result != 0:
                return result

    if not is_arr(left) and not is_arr(right):
        return 0 if left == right else 1 if left < right else -1

    raise Exception('should not make it here')




if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    part1_result = 0
    for i in range(0, len(lines), 3):
        left = parse_arr(lines[i])
        right = parse_arr(lines[i+1])
        result = compare_pairs(left, right)
        # print(f'Left {left} vs Right {right} -> {result}')
        if result == 1:
            part1_result += (i//3)+1

    print(f'Result 1: {part1_result}')

