def move_tail_1_step_closer_to_head(head, tail):
    if head[0] > tail[0] + 1:
        tail[0] += 1
        tail[1] = head[1]
    elif head[0] < tail[0] - 1:
        tail[0] -= 1
        tail[1] = head[1]

    if head[1] > tail[1] + 1:
        tail[1] += 1
        tail[0] = head[0]
    elif head[1] < tail[1] - 1:
        tail[1] -= 1
        tail[0] = head[0]


def convert_to_coord(lines):
    all_steps = []
    for dir, steps in lines:
        unit = 1
        delta = (unit, 0) if dir == "R" else (-unit, 0) if dir == "L" else (0, -unit) if dir == "D" else (0, unit)
        for step in range(steps):
            all_steps.append(delta)
    return all_steps


def main():
    with open('input.txt') as f:
        lines = [line.split() for line in f]
        lines = [[x[0], int(x[1])] for x in lines]

    coords = convert_to_coord(lines)

    head, tail = [0, 0], [0, 0]
    tail_visited = set()

    for dx, dy in coords:
        head[0] += dx
        head[1] += dy
        move_tail_1_step_closer_to_head(head, tail)
        tail_visited.add((tail[0], tail[1]))

    print(f'Result 1: {len(tail_visited)}')



if __name__ == '__main__':
    main()
