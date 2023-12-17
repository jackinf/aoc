with open('input.txt', 'r') as f:
    grid = [list(line) for line in f.read().split('\n')]


def count_occupied(grid, seen):
    occupied = 0
    for row in range(len(grid)):
        print()
        for col in range(len(grid[0])):

            if (row, col, -1, 0) in seen:
                print('#', end='')
                occupied += 1
            elif (row, col, 1, 0) in seen:
                print('#', end='')
                occupied += 1
            elif (row, col, 0, -1) in seen:
                print('#', end='')
                occupied += 1
            elif (row, col, 0, 1) in seen:
                print('#', end='')
                occupied += 1
            else:
                print('.', end='')
    print()
    return occupied


def is_oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


q = [(0, 0, (0, 1))]
seen = set()
while q:
    row, col, dir = q.pop(0)

    if is_oob(grid, row, col):
        continue

    if (row, col, dir[0], dir[1]) in seen:
        continue
    seen.add((row, col, dir[0], dir[1]))

    val = grid[row][col]
    # grid[row][col] = '#'

    if val == '.' or val == '-' and dir[0] == 0 or val == '|' and dir[1] == 0:
        if dir == (-1, 0): q.append((row - 1, col, dir))
        if dir == (1, 0): q.append((row + 1, col, dir))
        if dir == (0, -1): q.append((row, col - 1, dir))
        if dir == (0, 1): q.append((row, col + 1, dir))
    elif val == '-' and dir[1] == 0:   # goes vertically
        q.append((row, col - 1, (0, -1)))
        q.append((row, col + 1, (0, 1)))
    elif val == '|' and dir[0] == 0:  # goes horizontally
        q.append((row - 1, col, (-1, 0)))
        q.append((row + 1, col, (1, 0)))
    elif val == '\\':
        if dir == (-1, 0): q.append((row,  col - 1, (0, -1)))
        if dir == (1, 0): q.append((row,  col + 1, (0, 1)))
        if dir == (0, -1): q.append((row - 1, col, (-1, 0)))
        if dir == (0, 1): q.append((row + 1, col, (1, 0)))
    elif val == '/':
        if dir == (-1, 0): q.append((row,  col + 1, (0, 1)))
        if dir == (1, 0): q.append((row,  col - 1, (0, -1)))
        if dir == (0, -1): q.append((row + 1, col, (1, 0)))
        if dir == (0, 1): q.append((row - 1, col, (-1, 0)))


occupied = count_occupied(grid, seen)

print(f'Part 1: {occupied}')

