def oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))


# todo: bfs with priority queue
def increase_dfs(grid, row, col):
    grid[row][col] += 1
    flashes = 0

    if grid[row][col] == 10:
        flashes += 1

        for nrow, ncol in (
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1),
        ):
            if oob(grid, nrow, ncol):
                continue

            flashes += increase_dfs(grid, nrow, ncol)

    return flashes


def to_zeros(grid):
    target = len(grid) * len(grid[0])
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] >= 10:
                grid[row][col] = 0
                target -= 1
    return target == 0


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [list(map(int, list(line.strip()))) for line in f]

    res = 0
    step = 1
    while True:
        step_flashes = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                fl = increase_dfs(grid, row, col)
                step_flashes += fl
        res += step_flashes
        all_flashed = to_zeros(grid)

        if step == 100:
            print(f'Result 1: {res}')
        if all_flashed:
            print(f'Result 2: {step}')
            break
        step += 1
