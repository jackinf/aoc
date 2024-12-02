def try_contract_grid(grid, positions):  # TODO: modify positions
    def remove_rows(grid):
        while len(grid) > 0:
            if '#' in grid[0]:
                break
            grid.pop(0)

        while len(grid) > 0:
            if '#' in grid[-1]:
                break
            grid.pop()

    grid = [[x for x in row] for row in grid]
    remove_rows(grid)
    grid = list(zip(*grid[::-1]))  # rotate
    remove_rows(grid)

    # TODO: figure out how to rotate back. Currently I'm rotating 3 times in one direction for now
    grid = list(zip(*grid[::-1]))
    grid = list(zip(*grid[::-1]))
    grid = list(zip(*grid[::-1]))

    return grid