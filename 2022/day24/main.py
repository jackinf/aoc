def bfs(RC, grid, start, stop, step):
    ROWS, COLS = RC

    q = {start}

    while True:
        next_q = set()

        for row, col in q:
            for new_row, new_col in ((row, col + 1), (row + 1, col), (row, col), (row - 1, col), (row, col - 1)):

                # check if finished
                if (new_row, new_col) == stop:
                    return step

                # check if out of bounds
                if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                    continue

                # check if intersects with blizzard at certain step
                if grid[new_row][(new_col - step) % COLS] == ">" \
                        or grid[new_row][(new_col + step) % COLS] == "<" \
                        or grid[(new_row - step) % ROWS][new_col] == "v" \
                        or grid[(new_row + step) % ROWS][new_col] == "^":
                    continue

                next_q.add((new_row, new_col))

        q = next_q
        if not q:
            q.add(start)
        step += 1


if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [list(line.strip()) for line in f]
        # cut walls
        grid = [[col for col in row][1:-1] for row in grid][1:-1]

    RC = len(grid), len(grid[0])
    ROWS, COLS = RC

    start = (-1, 0)
    stop = (ROWS, COLS - 1)

    step1 = bfs(RC, grid, start, stop, 1)
    print(f'Result 1: {step1}')

    step2 = bfs(RC, grid, stop, start, step1)
    step3 = bfs(RC, grid, start, stop, step2)
    print(f'Result 2: {step3}')
