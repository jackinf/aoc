from heapq import heappush, heappop
from typing import Optional, Set, Tuple


def read_input(file_name: str):
    with open(file_name) as f:
        return [list(x) for x in f.read().split('\n')]

def find_paths(grid) -> Set[Set[Tuple[int, int]]]:
    start = next((row_i, col_i) for row_i, row in enumerate(grid) for col_i, cell in enumerate(row) if cell == 'S')
    end = next((row_i, col_i) for row_i, row in enumerate(grid) for col_i, cell in enumerate(row) if cell == 'E')

    # print(start, end)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    heap = [(0, 0, start[0], start[1], {start})]
    best_paths = set()
    visited = {}
    lowest_score: Optional[int] = None

    while heap:
        score, dir_i, row, col, path = heappop(heap)

        if grid[row][col] == '#':
            continue

        if lowest_score and lowest_score < score:
            break

        if (row, col) == end:
            lowest_score = score
            best_paths |= path
            continue

        visited_key = (row, col, dir_i)
        prev_score = visited.get(visited_key)
        if prev_score and prev_score < score:
            continue
        visited[visited_key] = score

        # go forward
        drow, dcol = directions[dir_i]
        nrow, ncol = row + drow, col + dcol
        heappush(heap, (score + 1, dir_i, nrow, ncol, path | {(nrow, ncol)}))

        # turn left
        heappush(heap, (score + 1000, (dir_i - 1) % 4, row, col, path))

        # turn right
        heappush(heap, (score + 1000, (dir_i + 1) % 4, row, col, path))

    return best_paths


def run():
    grid = read_input('input.txt')
    paths = find_paths(grid)
    print(f'Part 2: {len(paths)}')  # 489


if __name__ == '__main__':
    run()