if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [list(map(int, list(line.strip()))) for line in f]
    print(grid)

    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for nrow, ncol in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if not (0 <= nrow < len(grid) and 0 <= ncol < len(grid[0])):
                    continue

                if grid[nrow][ncol] <= grid[row][col]:
                    break
            else:
                res += grid[row][col] + 1

    print(f'Result 1: {res}')
