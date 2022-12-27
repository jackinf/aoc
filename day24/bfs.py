import heapq


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

    q = [(0, (0, 0), 1)]
    while q:
        # item = q.pop(0)
        item = heapq.heappop(q)
        score, (row, col), step = item
        print(f'\r q: {len(q)}', end='', flush=True)
        if not (0 <= row < ROWS and 0 <= col < COLS):
            continue

        # check if finished
        if row == ROWS - 1 and col == COLS - 2:
            print()
            print(f'best_steps: {step}')
            return step  # assume best step

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)):
            new_row, new_col = row + dr, col + dc
            if not is_occupied_at(RC, bpos_rev, new_row, new_col, step + 1):
                score = -(new_row * 100_000 + new_col)
                new_item = (score, (new_row, new_col), step + 1)
                heapq.heappush(q, new_item)
                # q.append(new_item)

    return -1
