import re


def draw_grid(grid):
    for row in grid:
        for col in row:
            print(col, end='')
        print()


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.read().split('\n')

    # parse instructions
    instructions = lines.pop()
    lines.pop()  # assume empty line
    instructions = re.findall(r'\d+|[RL]', instructions)

    # parse grid
    width, height = max(len(line) for line in lines), len(lines)
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            grid[row][col] = lines[row][col]

    draw_grid(grid)
    print()

    """
        1,  0 - right
        0,  1 - down
        -1, 0 - left
        0, -1 - up 
    """
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_i = 0
    get_turn_symbol = lambda: '>' if dir_i == 0 else 'v' if dir_i == 1 else '<' if dir_i == 2 else '^'

    def turn(dir: str):
        global dir_i
        if dir == 'R':
            dir_i += 1
        if dir == 'L':
            dir_i -= 1
        dir_i %= len(dirs)

    ROWS, COLS = len(grid), len(grid[0])
    curr_row = 0
    curr_col = lines[0].index('.')
    curr = [curr_row, curr_col]

    for move in instructions:
        if move.isalpha():
            turn(move)
            grid[curr_row][curr_col] = get_turn_symbol()
            continue

        steps = int(move)
        while steps > 0:
            steps -= 1
            delta_row, delta_col = dirs[dir_i]
            new_col, new_row = curr_col, curr_row

            # 1. out of bounds, wrap around. Continue moving till we find a surface
            while True:
                new_col = (new_col + delta_col) % COLS
                new_row = (new_row + delta_row) % ROWS
                if grid[new_row][new_col] != ' ':
                    break

            # 2. check for walls
            if grid[new_row][new_col] == '#':
                steps = 0
                continue

            curr_row = new_row
            curr_col = new_col
            grid[curr_row][curr_col] = get_turn_symbol()

    draw_grid(grid)

    print(f'Current row: {curr_row + 1}')
    print(f'Current col: {curr_col + 1}')
    print(f'Current dir: {dir_i}')

    password = (curr_row + 1) * 1000 + (curr_col + 1) * 4 + dir_i
    print(f'Result 1: {password}')
