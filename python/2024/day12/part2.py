from collections import defaultdict, Counter
from typing import Dict, Set, Tuple


def read_grid(file_path):
    with open(file_path) as f:
        lines = f.read().split('\n')
        grid = [list(line) for line in lines]
    return grid


def toggle_wall(wall, key, all_walls):
    if wall in all_walls[key]:
        all_walls[key].remove(wall)
    else:
        all_walls[key].add(wall)


def solve(row, col, symbol, key, grid, all_walls, ROWS, COLS):
    EMPTY = '.'
    NORTH, SOUTH, EAST, WEST = (-1, 0), (1, 0), (0, 1), (0, -1)

    # Check out of bounds
    if not (0 <= row < ROWS and 0 <= col < COLS):
        return 0

    # Check if the cell is already visited or not the target symbol
    if grid[row][col] != symbol:
        return 0

    grid[row][col] = EMPTY

    # Define walls
    walls = [
        (row + 0, col + 0, row + 1, col + 0),  # West wall
        (row + 0, col + 0, row + 0, col + 1),  # North wall
        (row + 0, col + 1, row + 1, col + 1),  # East wall
        (row + 1, col + 0, row + 1, col + 1),  # South wall
    ]

    for wall in walls:
        toggle_wall(wall, key, all_walls)

    # Count the current cell and explore neighbors
    areas_count = 1
    directions = [NORTH, SOUTH, EAST, WEST]
    for dr, dc in directions:
        areas_count += solve(row + dr, col + dc, symbol, key, grid, all_walls, ROWS, COLS)

    return areas_count


def count_corners(areas_dict, all_walls):
    total_result = 0
    for area_key, walls in all_walls.items():
        area = areas_dict[area_key]

        corners = 0
        while walls:
            x1, y1, x2, y2 = walls.pop()

            candidates = []
            if x1 == x2:
                x, y_start, y_end = x1, min(y1, y2), max(y1, y2)

                candidates.extend([
                    (x, y_start, x - 1, y_start),
                    (x - 1, y_start, x, y_start),
                    (x, y_start, x + 1, y_start),
                    (x + 1, y_start, x, y_start),

                    (x, y_end, x - 1, y_end),
                    (x - 1, y_end, x, y_end),
                    (x, y_end, x + 1, y_end),
                    (x + 1, y_end, x, y_end),
                ])

            if y1 == y2:
                y, x_start, x_end = y1, min(x1, x2), max(x1, x2)

                candidates.extend([
                    (x_start, y - 1, x_start, y),
                    (x_start, y, x_start, y - 1),
                    (x_start, y + 1, x_start, y),
                    (x_start, y, x_start, y + 1),

                    (x_end, y - 1, x_end, y),
                    (x_end, y, x_end, y - 1),
                    (x_end, y + 1, x_end, y),
                    (x_end, y, x_end, y + 1),
                ])

            common = walls & set(candidates)
            corners += len(common)

            # print(candidates)

        # count crosses - todo

        result = area * corners
        total_result += result

    return total_result


def count_corners2(areas_dict, all_walls):
    total_result = 0
    for area_key, walls in all_walls.items():
        area = areas_dict[area_key]

        connected = []

        turns = 0
        while walls:
            curr = walls.pop()
            for other in walls:
                if curr[0] == other[0] or curr[1] == other[1]:
                    pass


def main():
    file_path = 'sample2.txt'  # Change to the appropriate file path
    grid = read_grid(file_path)
    ROWS, COLS = len(grid), len(grid[0])

    all_walls: Dict[str, Set[Tuple[int, int]]] = defaultdict(set)
    areas_dict = {}

    for row in range(ROWS):
        for col in range(COLS):
            symbol = grid[row][col]
            if symbol != '.':
                key = symbol
                areas_count = solve(row, col, symbol, key, grid, all_walls, ROWS, COLS)
                areas_dict[key] = areas_count

    final_result = count_corners(areas_dict, all_walls)
    print(f'Part 2: {final_result}')


if __name__ == "__main__":
    main()
