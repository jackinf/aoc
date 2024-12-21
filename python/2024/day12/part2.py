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

        result = area * corners
        total_result += result

    return total_result


def count_crosses(grid, all_walls):
    ROWS, COLS = len(grid), len(grid[0])
    cross_count = 0

    for row in range(ROWS - 1):
        for col in range(COLS - 1):
            # Check if the grid cells satisfy the cross condition
            if (grid[row][col] == grid[row + 1][col + 1] and
                    grid[row][col + 1] == grid[row + 1][col] and
                    grid[row][col] != grid[row + 1][col]):

                # Define the walls to check
                wall_1 = (row + 1, col + 1, row + 1, col + 2)
                wall_2 = (row + 1, col + 2, row + 1, col + 3)
                wall_3 = (row, col + 1, row + 1, col + 1)
                wall_4 = (row, col + 1, row + 2, col + 1)

                # Check if all required walls are present
                key = grid[row][col]
                if (wall_1 in all_walls[key] or wall_1[::-1] in all_walls[key]) and \
                        (wall_2 in all_walls[key] or wall_2[::-1] in all_walls[key]) and \
                        (wall_3 in all_walls[key] or wall_3[::-1] in all_walls[key]) and \
                        (wall_4 in all_walls[key] or wall_4[::-1] in all_walls[key]):
                    cross_count += 1

    return cross_count


# the whole solution is wrong
def main():
    file_path = 'sample3.txt'  # Change to the appropriate file path
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

    print(all_walls)
    print(areas_dict)
    final_result = count_corners(areas_dict, all_walls)
    crosses_count = count_crosses(grid, all_walls)
    print(crosses_count)
    print(f'Part 2: {final_result - crosses_count}')


if __name__ == "__main__":
    main()
