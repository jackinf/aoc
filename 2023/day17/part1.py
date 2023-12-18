from collections import defaultdict

with open('input.txt', 'r') as f:
    grid = [list(map(int, list(line))) for line in f.read().split('\n')]


def is_oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


def debug(grid, seen):
    for row in range(len(grid)):
        print()
        for col in range(len(grid[0])):

            if (row, col) in seen:
                print(str(grid[row][col]), end='')
            else:
                print('.', end='')
    print()



turn_90deg = {
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0)
}

turn_90deg_neg = {
    (1, 0): (0, 1),
    (0, -1): (1, 0),
    (-1, 0): (0, -1),
    (0, 1): (-1, 0)
}


best = float('inf')
seen = defaultdict(lambda: float('inf'))
q = []
COUNTER = 1
# q.append((0, 0, -grid[0][0], (1, 0), COUNTER, []))
# q.append((0, 0, -grid[0][0], (0, 1), COUNTER, []))
q.append((0, 0, -grid[0][0], (1, 0), COUNTER))
q.append((0, 0, -grid[0][0], (0, 1), COUNTER))
while q:
    # row, col, heat, dir, counter, path = q.pop(0)
    row, col, heat, dir, counter = q.pop(0)

    if counter <= 0:
        continue

    if is_oob(grid, row, col):
        continue

    heat += grid[row][col]
    # path.append((row, col))

    if row == len(grid) - 1 and col == len(grid[0]) - 1 and best > heat:
        # debug(grid, path)
        # print(f'result: {heat}')
        best = heat
        continue

    key = (row, col, counter)
    if seen[key] < heat:
        continue
    seen[key] = heat

    # move forward
    # q.append((row + dir[0], col + dir[1], heat, dir, counter - 1, path[:]))
    q.append((row + dir[0], col + dir[1], heat, dir, counter - 1))

    # turn left
    new_dir1 = turn_90deg_neg[dir]
    # q.append((row + new_dir1[0], col + new_dir1[1], heat, new_dir1, 3, path[:]))
    q.append((row + new_dir1[0], col + new_dir1[1], heat, new_dir1, 3))

    # turn right
    new_dir2 = turn_90deg[dir]
    # q.append((row + new_dir2[0], col + new_dir2[1], heat, new_dir2, 3, path[:]))
    q.append((row + new_dir2[0], col + new_dir2[1], heat, new_dir2, 3))


print(f'Part 1: {best}')


