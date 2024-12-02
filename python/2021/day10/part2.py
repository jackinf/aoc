scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

br_map = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def is_corrupt(line):
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

        return True

    if st:
        # incomplete
        return False

    return False


def complete(line):
    st = []

    for ch in line:
        if ch in '{[(<':
            st.append(ch)
            continue

        if br_map[ch] == st[-1]:
            st.pop()
            continue

        raise Exception('should not happen 2')

    res = 0
    while st:
        res *= 5
        res += scores[st.pop()]

    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    lines = [line for line in lines if not is_corrupt(line)]

    res = sorted([complete(line) for line in lines])
    print(f'Result 2: {res[len(res) // 2]}')
