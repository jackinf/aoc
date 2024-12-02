if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    COLS = len(lines[0])
    counter = [0] * COLS

    for i in range(COLS):
        for line in lines:
            counter[i] += 1 if line[i] == '1' else 0

    oxygen = ''
    co2 = ''

    lines_ = lines[:]
    for i in range(COLS):
        if len(lines_) == 1:
            oxygen = lines_[0]
            break

        ones = sum(1 for line in lines_ if line[i] == '1')
        zeros = len(lines_) - ones

        if ones >= zeros:
            oxygen += '1'
            lines_ = [line for line in lines_ if line[i] == '1']
        else:
            oxygen += '0'
            lines_ = [line for line in lines_ if line[i] == '0']

    lines_ = lines[:]
    for i in range(COLS):
        if len(lines_) == 1:
            co2 = lines_[0]
            break

        ones = sum(1 for line in lines_ if line[i] == '1')
        zeros = len(lines_) - ones

        if ones >= zeros:
            co2 += '0'
            lines_ = [line for line in lines_ if line[i] == '0']
        else:
            co2 += '1'
            lines_ = [line for line in lines_ if line[i] == '1']

    oxygen_dec = int(oxygen, 2)
    co2_dec = int(co2, 2)
    res = oxygen_dec * co2_dec
    print(f'Result 2: {res}')
