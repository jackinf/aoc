if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.split() for line in f]

    increments = [0]

    while lines:
        items = lines.pop(0)

        if items[0] == "addx":
            increments.append(0)
            increments.append(0)
            increments[-1] = int(items[1])
            continue

        if items[0] == "noop":
            increments.append(0)
            continue

    values = [0] * len(increments)
    values[0] = 1
    for i in range(1, len(values)):
        values[i] = values[i-1] + increments[i]

    signal_strengths = []
    for i, value in enumerate(values):
        if (i - 20) % 40 == 0:
            print(f'{i} x {value} = {i * value}')
            signal_strengths.append(i * values[i-1])

    print(f'Result 1: {sum(signal_strengths)}')

