import heapq

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

seen = set()
best_row, best_col = 0, 0
q = []

# heat, row, col, delta row, delta col, move_counter
q.append((0, 0, 0, 0, 0, 4, []))
moves = 0
while q:
    moves += 1
    heat, row, col, drow, dcol, counter, path = heapq.heappop(q)
    path.append((row, col))

    if is_oob(grid, row, col):
        continue

    # for debug purposes
    best_row = max(best_row, row)
    best_col = max(best_col, col)
    print(f'q len = {len(q)}, best_row = {best_row} / {len(grid)}, best_col = {best_col} / {len(grid[0])}')

    if row == len(grid) - 1 and col == len(grid[0]) - 1 and counter >= 4:
        debug(grid, path)
        print(f'Part 2: {heat + 1}, moves: {moves}')
        break

    # optimization
    key = (row, col, drow, dcol, counter)
    if key in seen:
        continue
    seen.add(key)

    # every step costs
    new_heat = heat + grid[row][col]

    # move forward
    if counter < 10 and (drow, dcol) != (0, 0):
        heapq.heappush(q, (new_heat, row + drow, col + dcol, drow, dcol, counter + 1, path[:]))

    # turn
    if counter >= 4:
        for new_dr, new_dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # do not go forwards or backwards
            if (new_dr, new_dc) in ((drow, dcol), (-drow, -dcol)):
                continue

            heapq.heappush(q, (new_heat, row + new_dr, col + new_dc, new_dr, new_dc, 1, path[:]))
