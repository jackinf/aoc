def solve(line):
    right = line[1]
    lengths = [len(code) for code in right]
    return sum(1 for length in lengths if length in {2, 3, 4, 7})


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        lines = [line.split('|') for line in lines]
        lines = [(line[0].strip().split(), line[1].strip().split()) for line in lines]

    res = 0
    for line in lines:
        res += solve(line)

    print(f'Result 1: {res}')

    """
    0 - 6 seg
    1 - 2 seg
    2 - 5 seg
    3 - 5 seg
    4 - 4 seg
    5 - 5 seg
    6 - 6 seg
    7 - 3 seg
    8 - 7 seg
    9 - 6 seg
    
    unique - 1 (2s), 4 (4s), 7 (3s), 8 (7s)
    """