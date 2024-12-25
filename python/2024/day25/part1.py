def read_input(file_name: str):
    with open(file_name) as f:
        blocks = f.read().split('\n\n')

    locks = []
    keys = []
    for block in blocks:
        grid = [list(row) for row in block.split('\n')]
        if grid[0][0] == '.':
            keys.append(grid)
        else:
            locks.append(grid)

    return locks, keys

def assert_same_size(locks, keys):
    for lock in locks:
        for key in keys:
            assert len(lock) == len(key)

def does_fit(lock, key):
    for row in range(len(lock)):
        for col in range(len(lock[0])):
            if lock[row][col] == '#' and key[row][col] == '#':
                return False
    return True

def solve_naive(locks, keys):
    fits = 0

    for lock in locks:
        for key in keys:
            if does_fit(lock, key):
                fits += 1

    return fits


def run():
    locks, keys = read_input('input.txt')
    assert_same_size(locks, keys)
    fits = solve_naive(locks, keys)
    print(f'Part 1: {fits}')

if __name__ == '__main__':
    run()