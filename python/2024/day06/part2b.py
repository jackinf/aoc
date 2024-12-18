from itertools import cycle

def parse_grid(input_lines):
    """Parses the grid from input."""
    grid = {}
    for r, line in enumerate(input_lines):
        for c, char in enumerate(line):
            grid[(r, c)] = char
    return grid


def add_points(p1, p2):
    """Adds two points (tuples of coordinates)."""
    return p1[0] + p2[0], p1[1] + p2[1]


def draw_map(grid, marked=None):
    """
    Draws the grid with optional visited points and obstacles.
    Args:
        grid: The grid dictionary.
        marked: A set of points to mark as obstacles (optional).
    """
    if marked is None:
        marked = set()

    min_row = min(r for r, _ in grid.keys())
    max_row = max(r for r, _ in grid.keys())
    min_col = min(c for _, c in grid.keys())
    max_col = max(c for _, c in grid.keys())

    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            point = (r, c)
            if point in marked:
                print("O", end="")  # Mark obstacles
            else:
                print(grid.get(point, " "), end="")  # Draw grid or empty space
        print()
    print("=" * (max_col - min_col + 1))


def track_guard(grid):
    """
    Traverses the grid to determine if a loop occurs.
    Returns:
        - True and the visited path if there's no loop.
        - False and an empty set if a loop is detected.
    """
    OFFSETS = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    offset = next(OFFSETS)

    # Find the initial starting point
    loc = next(k for k, v in grid.items() if v == "^")
    visited = {(loc, offset)}

    while True:
        next_loc = add_points(loc, offset)
        if next_loc not in grid:
            # Exited the grid
            break

        if grid[next_loc] == "#":
            # Hit a wall; turn 90 degrees right
            offset = next(OFFSETS)
            visited.add((loc, offset))
        else:
            # Move forward and check for loops
            to_add = (next_loc, offset)
            if to_add in visited:
                # Detected a loop
                return False, set()

            visited.add(to_add)
            loc = next_loc

    # Successfully exited the grid
    return True, {l for l, _ in visited}


def solve(input_lines):
    """
    Main solver function.
    Returns:
        - Initial path size
        - Number of possible obstacle locations
    """
    grid = parse_grid(input_lines)

    # Get the initial path
    exited, path = track_guard(grid)
    assert exited
    initial_path_size = len(path)

    print("Initial Map with Path:")
    draw_map(grid, marked=path)

    possible_obstacle_locations = 0
    obstacle_points = set()

    for loc in path:
        # Only consider empty cells for obstacle placement
        if grid[loc] != ".":
            continue

        # Temporarily place a wall and check if it creates a loop
        grid[loc] = "#"
        exited, _ = track_guard(grid)
        if not exited:
            possible_obstacle_locations += 1
            obstacle_points.add(loc)
        # Revert the wall
        grid[loc] = "."

    print("Final Map with Obstacle Locations:")
    draw_map(grid, marked=obstacle_points)

    return initial_path_size, possible_obstacle_locations


# Example usage:
if __name__ == "__main__":
    with open("input.txt") as f:
        input_lines = f.read().splitlines()

    result = solve(input_lines)
    print(f"Part 1: {result[0]}")
    print(f"Part 2: {result[1]}")
