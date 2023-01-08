import heapq
import sys


def solve_bfs(grid):
    WIDTH, HEIGHT = len(grid[0]), len(grid)

    # score, risk, row, col, seen, depth
    q = [(0, 0, 0, 0, 0)]
    best_risk = sys.maxsize

    seen = {}

    while q:
        score, risk, row, col, depth = heapq.heappop(q)
        print(f'\rq={len(q)}, score={score}, risk={risk}, best_risk={best_risk}', end='', flush=True)

        key = (row, col)
        if key in seen and seen[key][0] <= risk:
            continue
        seen[key] = (risk, depth)

        if risk > best_risk:
            continue

        if row == WIDTH - 1 and col == HEIGHT - 1:
            best_risk = min(risk, best_risk)
            continue

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue

            new_risk = risk + grid[row][col]
            new_score = (WIDTH - 1 - nc) * (HEIGHT - 1 - nr)

            heapq.heappush(q, (0, new_risk, nr, nc, depth + 1))

    print()
    return best_risk


if __name__ == '__main__':
    with open('sample3.txt') as f:
        grid = [[int(x) for x in list(line.strip())] for line in f]

    res = solve_bfs(grid)
    print(f'Result 1: {res}')  # 1045 - too high, 653 - too low, 670 - too high


