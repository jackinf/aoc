import heapq
import sys
from collections import defaultdict


def solve_bfs(grid):
    WIDTH, HEIGHT = len(grid[0]), len(grid)

    risks = defaultdict(lambda: sys.maxsize)
    risks[(0, 0)] = 0
    visited = set()

    # risk, row, col
    q = [(0, 0, 0)]

    while q:
        risk, row, col = heapq.heappop(q)

        curr = (row, col)
        if curr in visited:
            continue
        visited.add(curr)

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue

            new_risk = min(risks[(nr, nc)], risks[curr] + grid[nr][nc])
            risks[(nr, nc)] = new_risk

            heapq.heappush(q, (new_risk, nr, nc))

    return risks[(HEIGHT - 1, WIDTH - 1)]


def expand(grid):
    EXP = 5
    width, height = len(grid[0]), len(grid)
    grid2 = [[0 for _ in range(width * EXP)] for _ in range(height * EXP)]

    # copy first square's value (square = 0th width & 0th height
    for row in range(height):
        for col in range(width):
            grid2[row][col] = grid[row][col]

    # then increase only 0th column values by 1
    for i in range(1, EXP):
        for row in range(i * height, (i+1) * height):
            for col in range(width):
                val = grid2[row - height][col]
                val += 1
                val = val if val <= 9 else 1
                grid2[row][col] = val

    # then traverse by rows, and increase accordingly
    for i in range(EXP):
        for j in range(EXP):
            if j == 0:
                continue

            for row in range(i * height, (i+1) * height):
                for col in range(j * width, (j+1) * width):
                    val = grid2[row][col - width]
                    val += 1
                    val = val if val <= 9 else 1
                    grid2[row][col] = val

    return grid2


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [[int(x) for x in list(line.strip())] for line in f]

    grid2 = expand(grid)

    # for row in range(len(grid2)):
    #     print()
    #     for col in range(len(grid2[0])):
    #         print(str(grid2[row][col]), end='')

    res = solve_bfs(grid2)
    print(f'Result 2: {res}')
