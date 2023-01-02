import re

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    parsed = [re.findall(r"(?P<dir>\w+) (?P<amount>\d+)", line)[0] for line in lines]
    moves = [(dir, int(amount)) for dir, amount, in parsed]

    part1 = [0, 0]
    for dir, amount in moves:
        if dir == "down":
            part1[0] += amount
        elif dir == "up":
            part1[0] -= amount
        else:
            part1[1] += amount

    print(f'Result 1: {part1[0] * part1[1]}')

    part2 = [0, 0]
    aim = 0
    for dir, amount in moves:
        if dir == "down":
            aim += amount
        elif dir == "up":
            aim -= amount
        else:
            part2[1] += amount
            part2[0] += aim * amount

    print(f'Result 2: {part2[0] * part2[1]}')
