with open('./input.txt') as f:
    grid = [[int(y) for y in x] for x in f.read().split('\n')]
    # print(grid)

ROWS, COLS = len(grid), len(grid[0])
starts = []

for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == 0:
            starts.append((row, col))

print(starts)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
END = 9
final_result = 0

def oob(row, col):
    return not (0 <= row < ROWS and 0 <= col < COLS)

for start_row, start_col in starts:
    result = 0
    q = [
        (start_row + UP[0], start_col + UP[1], 0),
        (start_row + DOWN[0], start_col + DOWN[1], 0),
        (start_row + LEFT[0], start_col + LEFT[1], 0),
        (start_row + RIGHT[0], start_col + RIGHT[1], 0),
    ]
    seen = set()

    while q:
        row, col, prev_value = q.pop(0)
        
        if not (0 <= row < ROWS and 0 <= col < COLS):
            continue

        curr_value = grid[row][col]
        if curr_value != prev_value + 1:
            continue

        if (row, col) in seen:
            continue
        seen.add((row, col))
        # print(row, col, prev_value)

        if curr_value == END:
            result += 1
            continue

        q.append((row + UP[0], col + UP[1], curr_value))
        q.append((row + DOWN[0], col + DOWN[1], curr_value))
        q.append((row + LEFT[0], col + LEFT[1], curr_value))
        q.append((row + RIGHT[0], col + RIGHT[1], curr_value))

    # print(result)
    final_result += result

print(f'Part 1: {final_result}')