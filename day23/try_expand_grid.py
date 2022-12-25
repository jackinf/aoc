def try_expand_grid(grid, positions):
    expand_amount = 1

    # check if N or S expansion is needed
    for col in range(len(grid[0])):
        if grid[0][col] != '#':
            continue

        for _ in range(expand_amount):
            grid.insert(0, ['.'] * len(grid[0]))

        for id, (row, col) in positions.items():
            positions[id] = (row + expand_amount, col)

        break

    for col in range(len(grid[0])):
        if grid[-1][col] != '#':
            continue

        for _ in range(expand_amount):
            grid.append(['.'] * len(grid[0]))

        break

    # check if E or W expansion is needed
    for row in range(len(grid)):
        if grid[row][0] != '#':
            continue

        for _ in range(expand_amount):
            for row2 in range(len(grid)):
                grid[row2].insert(0, '.')

        for id, (row, col) in positions.items():
            positions[id] = (row, col + expand_amount)

        break

    for row in range(len(grid)):
        if grid[row][-1] != '#':
            continue

        for _ in range(expand_amount):
            for row2 in range(len(grid)):
                grid[row2].append('.')
        break
