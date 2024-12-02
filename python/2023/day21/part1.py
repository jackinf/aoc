with open('input.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')

# cool way of finding a starting position
S = divmod(text.find('S'), len(lines) + 1)
grid = [list(line) for line in lines]

print(grid)


def debug(grid, seen, symbol='x'):
    for row in range(len(grid)):
        print()
        for col in range(len(grid[0])):

            if (row, col) not in seen:
                print(grid[row][col], end='')
            else:
                print(symbol, end='')
    print()


# define the border
q = [(*S, 0, [])]
seen = set()
border = set()
evens = set()
while q:
    row, col, depth, path = q.pop(0)
    path.append((row, col))

    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        continue

    if grid[row][col] == '#':
        continue

    if (row, col) in seen:
        continue
    seen.add((row, col))

    if depth % 2 == 0:
        evens.add((row, col))

    if depth == 64:
        border.add((row, col))
        continue

    for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        q.append((row + drow, col + dcol, depth + 1, path[:]))

debug(grid, border, 'x')
debug(grid, evens, 'O')

total = len(evens)
print(f'Part 1: {total}')