scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

br_map = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def solve(line):
    st = []

    for ch in line:
        if ch in '{[(<':
            st.append(ch)
            continue

        if not st:
            raise Exception('should not happen 1')

        if br_map[ch] == st[-1]:
            st.pop()
            continue

        return scores[ch]

    if st:
        # incomplete
        return 0

    return 0


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
    print(lines)

    res = 0
    for line in lines:
        res += solve(line)

    print(f'Result 1: {res}')
