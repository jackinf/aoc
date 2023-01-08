import heapq
import sys


def solve_bfs(grid):
    WIDTH, HEIGHT = len(grid[0]), len(grid)

    # score, risk, row, col, seen, depth
    q = [(0, 0, 0, 0, set(), 0)]
    best_risk = sys.maxsize
    while q:
        score, risk, row, col, seen, depth = heapq.heappop(q)
        print(f'\rq={len(q)}, best_risk={best_risk}', end='', flush=True)

        key = (row, col)
        if key in seen:
            continue
        seen.add(key)

        if risk > best_risk:
            continue

        if row == WIDTH - 1 and col == HEIGHT - 1:
            best_risk = min(risk, best_risk)
            continue

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue

            if (nr, nc) in seen:
                continue

            new_risk = risk + grid[row][col]
            new_score = depth + (WIDTH - nc) + (HEIGHT - nr)

            heapq.heappush(q, (new_score, new_risk, nr, nc, seen.copy(), depth + 1))

    print()
    return best_risk


if __name__ == '__main__':
    with open('sample.txt') as f:
        grid = [[int(x) for x in list(line.strip())] for line in f]

    res = solve_bfs(grid)
    print(f'Result 1: {res}')


