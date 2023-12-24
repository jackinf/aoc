from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    grid = [list(line) for line in lines]

# assuming starting position at (0, 1) coming from up (0, 1) and depth is 0, set is seen
q = [(0, 0, 1, {(0, 1)})]

LAST = (len(grid) - 1, len(grid[0]) - 2)


def debug(grid, seen, symbol='x'):
    for row in range(len(grid)):
        print()
        for col in range(len(grid[0])):

            if (row, col) not in seen:
                print(grid[row][col], end='')
            else:
                print(symbol, end='')
    print()


def get_directions(val):
    match val:
        case '#': return []
        case _: return [(-1, 0), (1, 0), (0, -1), (0, 1)]


max_depth = defaultdict(lambda: -1)
best_depth = 0
while q:
    depth, row, col, local_seen = q.pop(0)
    if (row, col) == LAST:
        # debug(grid, local_seen, symbol='O')
        print(f'depth = {depth}')
        best_depth = max(best_depth, depth)
        continue

    DIRECTIONS = get_directions(grid[row][col])
    should_copy_seen = False
    for drow, dcol in DIRECTIONS:
        nrow, ncol = row + drow, col + dcol
        if not (0 <= nrow < len(grid) and 0 <= ncol < len(grid[0])):
            continue

        if grid[nrow][ncol] == '#':
            continue

        if (nrow, ncol) in local_seen:
            continue

        if depth < max_depth[(nrow, ncol)]:
            continue
        max_depth[(nrow, ncol)] = depth

        # decided that the next cell is valid, thus queueing the next cell
        if should_copy_seen:
            # debug(grid, local_seen, symbol='O')
            local_seen = set(local_seen)
        should_copy_seen = True
        local_seen.add((nrow, ncol))
        q.append((depth + 1, nrow, ncol, local_seen))


print(f'Part 2: {best_depth}')
