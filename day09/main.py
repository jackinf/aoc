def move_tail_1_step_closer_to_head(head, tail):
    if head[0] > tail[0] + 1:
        tail[0] += 1

        if tail[1] < head[1]:
            tail[1] += 1
        if tail[1] > head[1]:
            tail[1] -= 1

    elif head[0] < tail[0] - 1:
        tail[0] -= 1

        if tail[1] < head[1]:
            tail[1] += 1
        if tail[1] > head[1]:
            tail[1] -= 1

    if head[1] > tail[1] + 1:
        tail[1] += 1

        if tail[0] < head[0]:
            tail[0] += 1
        if tail[0] > head[0]:
            tail[0] -= 1

    elif head[1] < tail[1] - 1:
        tail[1] -= 1

        if tail[0] < head[0]:
            tail[0] += 1
        if tail[0] > head[0]:
            tail[0] -= 1


def convert_to_coord(lines):
    all_steps = []
    for dir, steps in lines:
        unit = 1
        delta = (unit, 0) if dir == "R" else (-unit, 0) if dir == "L" else (0, -unit) if dir == "D" else (0, unit)
        for step in range(steps):
            all_steps.append(delta)
    return all_steps


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.split() for line in f]
        lines = [[x[0], int(x[1])] for x in lines]

    coords = convert_to_coord(lines)

    head = [0, 0]
    tails = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    tail_visited1 = set()
    tail_visited2 = set()

    for dx, dy in coords:
        head[0] += dx
        head[1] += dy
        for i in range(len(tails)):
            if i == 0:
                move_tail_1_step_closer_to_head(head, tails[0])
                tail_visited1.add((tails[0][0], tails[0][1]))
            else:
                move_tail_1_step_closer_to_head(tails[i - 1], tails[i])

            if i == 8:
                tail_visited2.add((tails[i][0], tails[i][1]))

    print(f'Result 1: {len(tail_visited1)}')
    print(f'Result 2: {len(tail_visited2)}')
