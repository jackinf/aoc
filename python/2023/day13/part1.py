with open('input.txt', 'r') as f:
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
def scan(pattern):
    global horizontals, verticals
    ROWS, COLS = len(pattern), len(pattern[0])

    # check verticals
    for col in range(COLS - 1):
        if is_vertically_symmetrical(pattern, col, col + 1):
            verticals.append(col + 1)

    # check horizontals
    for row in range(ROWS - 1):
        if is_horizontally_symmetrical(pattern, row, row + 1):
            horizontals.append(row + 1)


for pattern in patterns:
    scan(pattern)

verticals_total = sum(verticals)
horizontals_total = 100 * sum(horizontals)
total = horizontals_total + verticals_total

print(f'Part 1: {total}')