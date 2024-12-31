import collections

WALL = '#'
START = 'S'
END = 'E'

def read_input(file_name: str):
    with open(file_name) as f:
        return [list(line) for line in f.read().split('\n')]

def oob(grid, row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def get_path(grid):
    start = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == START)
    end = next((i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == END)

    print(start, end)

    # X - row, Y - col
    px, py = start
    cx, cy = start
    while grid[cx][cy] != END:
        yield cx, cy

        tx, ty = cx, cy
        cx, cy = next((nx, ny) for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1))
                      if grid[nx][ny] != WALL and (nx, ny) != (px, py))
        px, py = tx, ty

    yield end


def walk(path, max_allowed_cut):
    # calculate all the pairs in the path
    for i1, (row1, col1) in enumerate(path):
        for i2 in range(i1 + 1, len(path)):
            row2, col2 = path[i2]
            shortcut_distance = abs(row1 - row2) + abs(col1 - col2)
            normal_distance = i2 - i1  # what is the normal travel distance
            saved = normal_distance - shortcut_distance    # how much steps did we save

            # did we save anything at all, and if so, is the shortcut within allowed 100 steps
            if saved > 0 and shortcut_distance <= max_allowed_cut:
                yield saved


def run():
    grid = read_input("input.txt")
    path = list(get_path(grid))
    print(f'Grid size M x N: {len(grid) * len(grid[0])}')
    print(path)

    scores = list(walk(path, 20))
    final_score = sum(score >= 100 for score in scores)
    print(collections.Counter(scores))
    print(f'Part 2: {final_score}')

if __name__ == '__main__':
    run()