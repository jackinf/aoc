from typing import List, Tuple


def get_separator(lines: List[str]) -> int:
    for i, line in enumerate(lines):
        if line.strip() == '':
            return i
    return -1


def parse_stacks_lines(stacks_lines: List[str]) -> List[List[str]]:
    """
    Assume that we have these lines:

        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    First, we count the number of stacks (3 in this case).
    Then, we create a list of empty lists with the same length as the number of stacks.
    Then, we iterate over the lines and append the first character of each line to the corresponding list.
    """

    stacks: List[List[str]] = []
    for _ in stacks_lines.pop().split():
        stacks.append([])

    while stacks_lines:
        line = stacks_lines.pop() + ' '  # add extra space so that we have consistently "[X] " pattern
        for i in range(0, len(line), 4):
            if line[i] == '[':
                letter = line[i + 1]
                stacks[i // 4].append(letter)

    return stacks


def parse_moves(lines: List[str]) -> List[Tuple[int, int, int]]:
    """ Assume that every line has format 'move 1 from 2 to 1' """

    numbers = [[int(s) for s in txt.split() if s.isdigit()] for txt in lines]  # extract only numbers
    return [(x[0], x[1]-1, x[2]-1) for x in numbers]  # convert to 0-based indexes; assume only 3 elements


def make_moves(stacks: List[List[str]], moves: List[Tuple[int, int, int]]) -> None:
    for count, src_index, dest_index in moves:
        what_to_move = stacks[src_index][-count:]

        stacks[dest_index].extend(reversed(what_to_move))
        stacks[src_index] = stacks[src_index][:-count]


def get_topmost(stack: List[List[str]]) -> str:
    return ''.join([x[-1] for x in stack])


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.read().split('\n')]
        separator_index = get_separator(lines)
        stacks_lines, moves_lines = lines[:separator_index], lines[separator_index + 1:]

    stacks = parse_stacks_lines(stacks_lines)
    moves = parse_moves(moves_lines)
    make_moves(stacks, moves)

    print(f"Result 1: {get_topmost(stacks)}")
