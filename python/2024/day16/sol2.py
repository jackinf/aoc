import heapq
from sys import maxsize

# https://git.sr.ht/~murr/advent-of-code/tree/master/item/2024/16/p2.py
maze = open("in.txt").read().splitlines()

seen = [[[maxsize for _ in range(4)] for x in range(len(maze[0]))] for y in range(len(maze))]

velocities = [(-1, 0), (0, 1), (1, 0), (0, -1)]

start_pos = None
end_pos = None
for j, r in enumerate(maze):
    for i, c in enumerate(r):
        if c == 'S':
            start_pos = (j, i)
        if c == 'E':
            end_pos = (j, i)

# TODO For C, need a better track of path than shoving it all into a list lmao
# I saw on da reddit a lot of folks searching backwards through the maze scores
# for all scores where score is -1 or -1001 from current, starting at end.
pq = [(0, (*start_pos, 1), [start_pos])] # start facing EAST
paths = []
best_score = maxsize

while pq and pq[0][0] <= best_score:
    score, (y, x, dir), path = heapq.heappop(pq)

    if (y, x) == end_pos:
        best_score = score
        paths.append(path)
        continue

    if seen[y][x][dir] < score:
        continue
    seen[y][x][dir] = score

    for i in range(4):
        dy, dx = velocities[i]
        ny, nx = y + dy, x + dx
        if maze[ny][nx] != '#' and (ny, nx) not in path:
            cost = 1 if i == dir else 1001
            heapq.heappush(pq, (score + cost, (ny, nx, i), path + [(ny, nx)]))

seats = set()
for path in paths:
    seats |= set(path)
print(len(seats))