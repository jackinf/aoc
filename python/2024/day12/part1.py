from collections import defaultdict
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

def calculate_result(areas_dict, all_walls):
    final_result = 0
    for area_key, areas_count in areas_dict.items():
        wall_count = len(all_walls[area_key])
        final_result += wall_count * areas_count
    return final_result

def main():
    file_path = 'input.txt'
    grid = read_grid(file_path)
    ROWS, COLS = len(grid), len(grid[0])

    all_walls: Dict[str, Set[Tuple[int, int]]] = defaultdict(set)
    areas_dict = {}

    for row in range(ROWS):
        for col in range(COLS):
            symbol = grid[row][col]
            if symbol != '.':
                key = f"{row * 10000000 + col}{symbol}"
                areas_count = solve(row, col, symbol, key, grid, all_walls, ROWS, COLS)
                areas_dict[key] = areas_count

    final_result = calculate_result(areas_dict, all_walls)
    print(f'Part 1: {final_result}')

if __name__ == "__main__":
    main()
