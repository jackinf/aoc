with open('python/2024/day12/input.txt') as f:
    lines = f.read().split('\n')
    grid = [list(x) for x in lines]
    # print(grid)

ROWS, COLS = len(grid), len(grid[0])
EMPTY = '.'
NORTH, SOUTH, EAST, WEST = (-1, 0), (1, 0), (0, 1), (0, -1)

# wall constants
SAME, RIGHT, DOWN, RIGHT_DOWN = (0, 0), (0, 1), (1, 0), (1, 1)

# from type import Dict, Set, Tuple
from collections import defaultdict
from typing import Dict, Set, Tuple

all_walls: Dict[str, Set[Tuple[int, int]]] = defaultdict(set)
# all_cells: Dict[str, Set[Tuple[int, int]]] = defaultdict(set)

def solve(row, col, symbol, key):
    global all_walls, all_cells, grid

    # check out of bounds
    if not (0 <= row < ROWS and 0 <= col < COLS):
        return 0

    # check if we have already visited this cell
    if grid[row][col] != symbol:
        return 0
    grid[row][col] = EMPTY
     
    # all_cells[key].add((row, col))

    # count all walls around the cells. toggle the wall if there is one nearby
    # for wall in ((cell + SAME, cell + RIGHT, cell + DOWN, cell + RIGHT_DOWN)):

    walls = [
        # west wall
        (row + 0, col + 0, row + 1, col + 0),  
        
        # north wall
        (row + 0, col + 0, row + 0, col + 1),
        
        # east wall
        (row + 0, col + 1, row + 1, col + 1),
        
        # south wall
        (row + 1, col + 0, row + 1, col + 1),
    ]

    for wall in walls:
        if wall in all_walls[key]:
            all_walls[key].remove(wall)
        else:
            all_walls[key].add(wall)

    # count that the current cell was visited
    areas_count = 1

    # go west, east, north, south
    areas_count += solve(row + NORTH[0], col + NORTH[1], symbol, key)
    areas_count += solve(row + SOUTH[0], col + SOUTH[1], symbol, key)
    areas_count += solve(row + EAST[0], col + EAST[1], symbol, key)
    areas_count += solve(row + WEST[0], col + WEST[1], symbol, key)

    return areas_count


areas_dict = {}
for row in range(ROWS):
    for col in range(COLS):
        symbol = grid[row][col]
        if symbol != EMPTY:
            # remember the cell. as there can be multiple of
            key = str(row * 10000000 + col) + symbol

            areas_count = solve(row, col, symbol, key)
            areas_dict[key] = areas_count
            

# print(areas_dict)
# print(all_walls)

final_result = 0
for area_key, areas_count in areas_dict.items():
    walls = all_walls[area_key]
    wall_count = len(walls)
    # print(area_key, areas_count, wall_count)
    result = wall_count * areas_count
    # print(result)
    final_result += result

print(f'Part 1: {final_result}')