import sys
from typing import Tuple, Dict

from day23.try_contract_grid import try_contract_grid
from day23.try_expand_grid import try_expand_grid


def paint_grid(grid):
    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [list(line.strip()) for line in f]

    # (row, col) - N, S, W, E
    directions_map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    directions_check_map = [
        [(-1, -1), (-1, 0), (-1, 1)],  # N -> NW, N, NE
        [(1, -1), (1, 0), (1, 1)],  # S -> SW, S, SE
        [(-1, -1), (0, -1), (1, -1)],  # W -> NW, W, SW
        [(-1, 1), (0, 1), (1, 1)],  # E -> NE, E, SE
    ]
    start_dir_id = 0

    positions = {}
    next_id = 1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                positions[next_id] = (row, col)
                next_id += 1

    def next_dirs(dir_id):
        dir_id %= len(directions_check_map)

        dir = directions_map[dir_id]
        check_dirs = directions_check_map[dir_id]

        return dir, check_dirs

    try_expand_grid(grid, positions)
    paint_grid(grid)
    print()

    round = 0
    while True:
        round += 1
        print(f'Round {round}')

        ROWS, COLS = len(grid), len(grid[0])

        # prepare the move (validate & place into candidate moves)
        candidates: Dict[Tuple[int, int], int] = {}
        all_elves_have_no_neighbors = True
        for id, (row, col) in positions.items():
            # check if not surrounded
            current_elf_has_no_neighbors = True
            for drow, dcol in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if grid[row + drow][col + dcol] == "#":
                    current_elf_has_no_neighbors = False
                    all_elves_have_no_neighbors = False

            # If no other Elves are in one of those eight positions, the Elf does not do anything
            if current_elf_has_no_neighbors:
                continue

            # attempt to move in one of the directions
            attempts = 0
            while attempts < 4:
                dir, check_dirs = next_dirs(start_dir_id + attempts)
                ok = True
                for drow, dcol in check_dirs:
                    if grid[row + drow][col + dcol] == "#":
                        ok = False

                if ok:
                    new_row, new_col = row + dir[0], col + dir[1]
                    if (new_row, new_col) in candidates:
                        candidates[(new_row, new_col)] = -1  # conflict, mark as invalid
                    else:
                        candidates[(new_row, new_col)] = id
                    break

                attempts += 1

        start_dir_id += 1

        if all_elves_have_no_neighbors:
            print('all elves are isolated', round)
            break

        # commit the move
        for (new_row, new_col), id in candidates.items():
            if id == -1:
                continue

            old_row, old_col = positions[id]
            positions[id] = (new_row, new_col)

            grid[old_row][old_col] = '.'
            grid[new_row][new_col] = "#"

        try_expand_grid(grid, positions)

    grid = try_contract_grid(grid, positions)
    paint_grid(grid)

    def calc(grid):
        elves = len([x for y in grid for x in y if x == '#'])
        return len(grid) * len(grid[0]) - elves

    part1 = calc(grid)
    print(f'Result 1: {part1}')
