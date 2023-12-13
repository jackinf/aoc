with open('sample.txt', 'r') as f:
    patterns = [[list(x) for x in pattern.split('\n')] for pattern in f.read().split('\n\n')]


def is_vertically_symmetrical(grid, col1, col2):
    while col1 >= 0 and col2 < len(pattern[0]):
        for row in range(len(grid)):
            if grid[row][col1] != grid[row][col2]:
                return False
        col1 -= 1
        col2 += 1
    return True


def is_horizontally_symmetrical(grid, row1, row2):
    while row1 >= 0 and row2 < len(pattern):
        for col in range(len(grid[0])):
            if grid[row1][col] != grid[row2][col]:
                return False
        row1 -= 1
        row2 += 1
    return True

verticals, horizontals = [], []
for pattern in patterns:
    # check verticals
    ROWS, COLS = len(pattern), len(pattern[0])

    res1 = is_vertically_symmetrical(pattern, COLS // 2 - 1, COLS // 2)
    if res1:
        verticals.append(COLS // 2)
    res2 = is_vertically_symmetrical(pattern, COLS // 2, COLS // 2 + 1) if COLS % 2 == 1 else False
    if res2:
        verticals.append(COLS // 2 + 1)

    # check horizontals
    res3 = is_horizontally_symmetrical(pattern, ROWS // 2 - 1, ROWS // 2)
    if res3:
        horizontals.append(ROWS // 2)
    res4 = is_horizontally_symmetrical(pattern, ROWS // 2, ROWS // 2 + 1) if ROWS % 2 == 1 else False
    if res4:
        horizontals.append(ROWS // 2 + 1)

verticals_total = sum(verticals)
horizontals_total = 100 * sum(horizontals)
total = horizontals_total + verticals_total
print(f'Part 1: {total}')