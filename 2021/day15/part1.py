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


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [[int(x) for x in list(line.strip())] for line in f]

    res = solve_bfs(grid)
    print(f'Result 1: {res}')
