def solve(line):
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

    left = [set(code) for code in line[0]]
    right = [set(code) for code in line[1]]

    n1 = next(code for code in left if len(code) == 2)
    n4 = next(code for code in left if len(code) == 4)
    n7 = next(code for code in left if len(code) == 3)
    n8 = next(code for code in left if len(code) == 7)

    n3 = next(code for code in left if len(code) == 5 and code & n7 == n7)
    n9 = next(code for code in left if len(code) == 6 and code & n3 == n3)
    n8m1 = n8 ^ n1
    n6 = next(code for code in left if len(code) == 6 and code & n8m1 == n8m1)
    n0 = next(code for code in left if len(code) == 6 and code != n6 and code != n9)
    n5 = next(code for code in left if len(code) == 5 and code & n6 == code)
    n2 = next(code for code in left if len(code) == 5 and code != n3 and code != n5)

    # print(f"{''.join(n0)}: 0")
    # print(f"{''.join(n1)}: 1")
    # print(f"{''.join(n2)}: 2")
    # print(f"{''.join(n3)}: 3")
    # print(f"{''.join(n4)}: 4")
    # print(f"{''.join(n5)}: 5")
    # print(f"{''.join(n6)}: 6")
    # print(f"{''.join(n7)}: 7")
    # print(f"{''.join(n8)}: 8")
    # print(f"{''.join(n9)}: 9")

    def map(code):
        if code == n0: return 0
        if code == n1: return 1
        if code == n2: return 2
        if code == n3: return 3
        if code == n4: return 4
        if code == n5: return 5
        if code == n6: return 6
        if code == n7: return 7
        if code == n8: return 8
        if code == n9: return 9
        return -1

    ans = [map(code) for code in right]
    ans = [str(x) for x in ans]
    ans = int(''.join(ans))

    return ans


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        lines = [line.split('|') for line in lines]
        lines = [(line[0].strip().split(), line[1].strip().split()) for line in lines]

    res = 0
    for i, line in enumerate(lines):
        res += solve(line)

    print(f'Result 2: {res}')
