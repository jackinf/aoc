import math

seen = set()


def oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def dfs(grid, row, col):
    key = (row, col)
    if key in seen:
        return 0
    seen.add(key)

    res = 1
    for nrow, ncol in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
        if oob(grid, nrow, ncol):
            continue

        if grid[nrow][ncol] == 9:
            continue

        res += dfs(grid, nrow, ncol)

    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [list(map(int, list(line.strip()))) for line in f]
    print(grid)

    basins = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for nrow, ncol in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if oob(grid, nrow, ncol):
                    continue

                if grid[nrow][ncol] <= grid[row][col]:
                    break
            else:
                # low point, calculate basin size
                res = dfs(grid, row, col)
                basins.append(res)

    res = math.prod(sorted(basins, reverse=True)[:3])
    print(f'Result 2: {res}')
