def is_occupied_at(RC, bpos_rev, row, col, step):
    ROWS, COLS = RC

    # consider cell occupied if it's a wall - possible only when out-of-bounds
    if not (0 <= row < ROWS and 0 <= col < COLS):
        return True

    # check down
    if "^" in bpos_rev.get(((row + step) % ROWS, col), set()):
        return True

    # check up
    if "v" in bpos_rev.get(((row - step) % ROWS, col), set()):
        return True

    # check right
    if "<" in bpos_rev.get((row, (col + step) % COLS), set()):
        return True

    # check left
    if ">" in bpos_rev.get((row, (col - step) % COLS), set()):
        return True

    return False


def bfs(RC, bpos_rev):
    ROWS, COLS = RC

    q = [((0, 0), 1)]
    while q:
        item = q.pop(0)
        (row, col), step = item
        print(f'\r q: {len(q)}', end='', flush=True)
        if not (0 <= row < ROWS and 0 <= col < COLS):
            continue

        # check if finished
        if row == ROWS - 1 and col == COLS - 2:
            print(f'best_steps: {step}')
            return step  # assume best step

        can_go_down = not is_occupied_at(RC, bpos_rev, row + 1, col, step + 1)
        can_go_right = not is_occupied_at(RC, bpos_rev, row, col + 1, step + 1)
        can_go_up = not is_occupied_at(RC, bpos_rev, row - 1, col, step + 1)
        can_go_left = not is_occupied_at(RC, bpos_rev, row, col - 1, step + 1)
        can_stay = not is_occupied_at(RC, bpos_rev, row, col, step + 1)

        if can_go_down:
            q.append(((row + 1, col), step + 1))
        if can_go_right:
            q.append(((row, col + 1), step + 1))

        if can_go_up:
            q.append(((row - 1, col), step + 1))
        if can_go_left:
            q.append(((row, col - 1), step + 1))
        if can_stay:
            q.append(((row, col), step + 1))

    return -1
