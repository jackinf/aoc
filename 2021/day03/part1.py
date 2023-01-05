if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(lines)

    COLS = len(lines[0])
    counter = [0] * COLS

    for i in range(COLS):
        for line in lines:
            counter[i] += 1 if line[i] == '1' else 0

    gamma = ''
    eps = ''

    for i in range(COLS):
        if counter[i] > len(lines) // 2:
            gamma += '1'
            eps += '0'
        else:
            gamma += '0'
            eps += '1'

    res = int(gamma, 2) * int(eps, 2)
    print(f'Result 1: {res}')
