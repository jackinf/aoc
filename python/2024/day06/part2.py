with open('input.txt') as f:
    grid = [list(x) for x in f.read().splitlines()]

# Find x, y position of ^ character
cx, cy = next((y, x) for y, row in enumerate(grid) for x, val in enumerate(row) if val == '^')
grid[cx][cy] = '.'

# Directions: up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_index = 0  # Initial direction index

def debug_grid():
    """Print the grid with successful enclosures marked."""
    print()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in horizontally_visited and (row, col) not in vertically_visited:
                print('-', end='')
            elif (row, col) not in horizontally_visited and (row, col) in vertically_visited:
                print('|', end='')
            elif (row, col) in horizontally_visited and (row, col) in vertically_visited:
                print('+', end='')
            else:
                print(grid[row][col], end='')
        print()
    print('====')
    print()


def debug_grid_enclosures():
    """Print the grid with successful enclosures marked."""
    print()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in successful_enclosures:
                print('O', end='')
            else:
                print(grid[row][col], end='')
        print()
    print('====')
    print()

# State tracking
visited = set()
horizontally_visited = set()
vertically_visited = set()
already_tested_enclosures = set()
successful_enclosures = set()
tx, ty, t_dir = None, None, None  # Tracking enclosure test state

def reset():
    """Reset the current enclosure test."""
    global cx, cy, dir_index, tx, ty, t_dir, horizontally_visited, vertically_visited
    cx, cy, dir_index = tx, ty, t_dir
    tx, ty, t_dir = None, None, None
    visited.clear()
    horizontally_visited.clear()
    vertically_visited.clear()


while True:
    dx, dy = directions[dir_index]
    nx, ny = cx + dx, cy + dy  # Calculate next position
    is_horizontal = dy != 0  # Check if the move is horizontal

    if tx is not None:
        if is_horizontal:
            horizontally_visited.add((cx, cy))
        else:
            vertically_visited.add((cx, cy))

    # Out-of-bounds check
    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
        if tx is not None:  # If testing an enclosure, reset state
            reset()
            continue
        break  # End simulation if out of bounds and not testing

    # Handle walls (#)
    if grid[nx][ny] == '#':
        dir_index = (dir_index + 1) % len(directions)  # Rotate 90° clockwise
        continue

    # Handle empty cells (.)
    if grid[nx][ny] == '.':
        # Check if we are in the loop
        if tx is not None:
            if is_horizontal and (nx, ny) in horizontally_visited:
                # debug_grid()
                successful_enclosures.add((tx + dx, ty + dy))
                reset()
                continue
            if not is_horizontal and (nx, ny) in vertically_visited:
                # debug_grid()
                successful_enclosures.add((tx + dx, ty + dy))
                reset()
                continue

        # Start testing a new potential enclosure
        if tx is None and (nx, ny) not in already_tested_enclosures:
            already_tested_enclosures.add((nx, ny))
            tx, ty, t_dir = cx, cy, dir_index  # Save current state for testing
            dir_index = (dir_index + 1) % len(directions)  # Rotate to test enclosure
            if is_horizontal:
                horizontally_visited.add((cx, cy))
            else:
                vertically_visited.add((cx, cy))
            continue

        # Move to the next cell
        cx, cy = nx, ny
        continue

    raise Exception(f'Unsupported cell type at ({nx}, {ny}): {grid[nx][ny]}')

# Debug output
# debug_grid_enclosures()
print(f'Part 2: {len(successful_enclosures)} loops found')
