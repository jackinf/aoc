import sys
from pprint import pprint

if __name__ == '__main__':
    with open('sample2.txt') as f:
        grid = [[int(x) for x in list(line.strip())] for line in f]

    width, height = len(grid[0]), len(grid)

    distances = [[sys.maxsize for col in range(width)] for row in range(height)]
    distances[0][0] = grid[0][0]

    q = [(0, 1), (1, 0)]
    while q:
        row, col = q.pop(0)
        if not (0 <= row < height and 0 <= col < width):
            continue

        left, up = sys.maxsize, sys.maxsize
        if 0 <= col - 1 < width and 0 <= row < height:
            left = distances[row][col - 1]

        if 0 <= col < width and 0 <= row - 1 < height:
            up = distances[row - 1][col]

        new_distance = min(left, up) + grid[row][col]
        if new_distance < distances[row][col]:
            distances[row][col] = new_distance

            q.append((row + 1, col))
            q.append((row, col + 1))

    pprint(distances)

    res = distances[-1][-1] - distances[0][0]
    print(f'Result 1: {res}')


