import sys
from typing import List, Tuple


def to_grid(lines: List[str]):
    start, end = None, None
    grid: List[List[str]] = [['' for _ in range(len(lines[0]))] for _ in range(len(lines))]
    for row, line in enumerate(lines):
        for col, item in enumerate(list(line)):
            if item == "S":
                start = [row, col]
                grid[row][col] = 'a'
                continue

            if item == "E":
                end = [row, col]
                grid[row][col] = 'z'
                continue

            grid[row][col] = item
    return grid, start, end


def find_min_steps(grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    q = [(tuple(start), 0)]

    endx, endy = end
    seen = set()

    while q:
        curr, depth = q.pop(0)
        currx, curry = curr[0], curr[1]
        if (currx, curry) in seen:
            continue
        seen.add((currx, curry))

        curr_val = ord(grid[currx][curry])
        if currx == endx and curry == endy:
            return depth

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            newx, newy = currx + dx, curry + dy
            if not (0 <= newx < len(grid) and 0 <= newy < len(grid[0])):
                continue

            if curr_val + 1 < ord(grid[newx][newy]):
                continue

            q.append([(newx, newy), depth + 1])

    return sys.maxsize


def find_all_a_positions(grid):
    positions = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'a':
                positions.append((row, col))
    return positions


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    grid, start, end = to_grid(lines)

    min_steps = find_min_steps(grid, tuple(start), tuple(end))
    print(f'Result 1: {min_steps}')

    best_min_steps = min_steps
    all_a_positions = find_all_a_positions(grid)
    for a_pos in all_a_positions:
        new_min_steps = find_min_steps(grid, tuple(a_pos), tuple(end))
        if new_min_steps < best_min_steps:
            best_min_steps = new_min_steps
    print(f'Result 2: {best_min_steps}')





