from day23.try_contract_grid import try_contract_grid


def check_case1():
    grid = [
        ['.', '.', '.', '.'],
        ['.', '#', '#', '.'],
        ['.', '.', '#', '.'],
        ['.', '.', '.', '.'],
    ]

    grid = try_contract_grid(grid, {})
    grid = try_contract_grid(grid, {})

    assert grid == [
        ('#', '#'),
        ('.', '#'),
    ]

if __name__ == '__main__':
    check_case1()
