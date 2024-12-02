import re


def parse(lines):
    coordinates = []
    while lines[0] != '':
        x, y = lines.pop(0).split(',')
        coordinates.append([int(x), int(y)])

    lines.pop(0)

    instructions = []
    while lines:
        line = lines.pop(0)
        match = re.search(r'fold along (?P<coord>\w)=(?P<num>\d+)', line)
        instructions.append((match.group('coord'), int(match.group('num'))))

    return coordinates, instructions


def draw_board(coordinates, width, height):
    dots_count = 0
    coordinates_set = {tuple(coord) for coord in coordinates}
    for row in range(height + 1):
        print()
        for col in range(width + 1):
            if (col, row) not in coordinates_set:
                print('.', end='')
            else:
                dots_count += 1
                print('#', end='')
    print()
    print(f'Dots count: {len(coordinates_set)} or {dots_count}')


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    coordinates, instructions = parse(lines)
    cols = [coord[0] for coord in coordinates]
    rows = [coord[1] for coord in coordinates]
    width = max(cols)
    height = max(rows)


    """
    
    y = 10
    0 1 2 3 4 5 6 7 8 9 | 10 11 12 13 14
    
    0 1 2 3 4 5  6   7   8   9
              14 13  12  11  10
    
    """

    steps = 1
    while instructions:
        instr_xy, instr_amount = instructions.pop(0)
        # draw_board(coordinates, width, height)

        # fold left
        if instr_xy == 'x':
            for coord in coordinates:
                if coord[0] >= instr_amount:
                    delta = coord[0] - instr_amount
                    delta *= 2
                    coord[0] = coord[0] - delta
            width = instr_amount

        # fold up
        if instr_xy == 'y':
            for coord in coordinates:
                if coord[1] >= instr_amount:
                    delta = coord[1] - instr_amount
                    delta *= 2
                    coord[1] = coord[1] - delta
            height = instr_amount

        # remove dupes
        coordinates = [[coord[0], coord[1]] for coord in list(set([tuple(coord) for coord in coordinates]))]

        if steps == 1:
            dots_count = len({tuple(coord) for coord in coordinates})
            print(f'Result 1: {dots_count}')
        steps += 1

    draw_board(coordinates, width, height)  # Result 2: I can read letters: HZLEHJRK
