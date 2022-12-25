from day23.try_expand_grid import try_expand_grid


def check_case1():
    grid = [
        ['#', '#'],
        ['.', '#'],
    ]

    try_expand_grid(grid, {})
    try_expand_grid(grid, {})
    try_expand_grid(grid, {})

    assert grid == [
        ['.', '.', '.', '.'],
        ['.', '#', '#', '.'],
        ['.', '.', '#', '.'],
        ['.', '.', '.', '.'],
    ]


def check_case2():
    grid = [
        ['#'],
    ]

    try_expand_grid(grid, {})
    try_expand_grid(grid, {})
    try_expand_grid(grid, {})

    assert grid == [
        ['.', '.', '.'],
        ['.', '#', '.'],
        ['.', '.', '.'],
    ]


if __name__ == '__main__':
    check_case1()
    check_case2()

