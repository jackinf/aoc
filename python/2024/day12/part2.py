from typing import List, Set, Tuple

NORTH, SOUTH, EAST, WEST = (-1, 0), (1, 0), (0, 1), (0, -1)
EMPTY = '.'

GRID = List[List[str]]

def read_grid(file_path):
    with open(file_path) as f:
        lines = f.read().split('\n')
        grid = [list(line) for line in lines]
    return grid

def oob(grid, row, col) -> bool:
    return not (0 <= row < len(grid) and 0 <= col < len(grid[row]))

def get(grid: list[list[str]], row: int, col: int) -> str | None:
    return None if oob(grid, row, col) else grid[row][col]

"""
n00 n01 n02
n10 n11 n12
n20 n21 n22
"""
def count_corners(grid: GRID, row: int, col: int) -> int:
    n00, n01, n02 = get(grid, row - 1, col - 1), get(grid, row - 1, col + 0), get(grid, row - 1, col + 1)
    n10, n11, n12 = get(grid, row + 0, col - 1), get(grid, row + 0, col + 0), get(grid, row + 0, col + 1)
    n20, n21, n22 = get(grid, row + 1, col - 1), get(grid, row + 1, col + 0), get(grid, row + 1, col + 1)

    total_corner_count = 0

    # open corners - two neighbors are same, and diagonally is different
    if n11 == n10 and n11 == n01 and n11 != n00:
        total_corner_count += 1
    if n11 == n12 and n11 == n01 and n11 != n02:
        total_corner_count += 1
    if n11 == n10 and n11 == n21 and n11 != n20:
        total_corner_count += 1
    if n11 == n12 and n11 == n21 and n11 != n22:
        total_corner_count += 1

    # closed corners
    if n11 != n10 and n11 != n01:
        total_corner_count += 1
    if n11 != n12 and n11 != n01:
        total_corner_count += 1
    if n11 != n10 and n11 != n21:
        total_corner_count += 1
    if n11 != n12 and n11 != n21:
        total_corner_count += 1

    return total_corner_count


def solve(grid: GRID, row: int, col: int, symbol: str, seen: Set[Tuple[int, int]]):
    # Check out of bounds
    if oob(grid, row, col):
        return 0, 0

    # Check if the cell is already visited or not the target symbol
    if (row, col) in seen or grid[row][col] != symbol:
        return 0, 0
    seen.add((row, col))

    total_areas = 1
    total_corners = count_corners(grid, row, col)

    for dr, dc in (NORTH, SOUTH, EAST, WEST):
        areas, corners = solve(grid, row + dr, col + dc, symbol, seen)
        total_areas += areas
        total_corners += corners

    return total_areas, total_corners


def main():
    grid = read_grid('input.txt')
    height, width = len(grid), len(grid[0])

    final_result = 0
    seen = set()
    for row in range(height):
        for col in range(width):
            symbol = grid[row][col]
            if symbol != '.':
                areas_count, corners_count = solve(grid, row, col, symbol, seen)
                final_result += areas_count * corners_count

    print(f'Part 2: {final_result}')


if __name__ == "__main__":
    main()

# 475096 - too low