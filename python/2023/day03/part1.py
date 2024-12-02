with open('input.txt') as f:
    whole_text = f.read()
    grid = [list(line) for line in whole_text.split('\n')]

special_symbols = [x for x in set(whole_text) if x not in ['.', '\n'] and not x.isnumeric()]


def is_oob(grid_, rowi_, coli_):
    return rowi_ < 0 or coli_ < 0 or len(grid_) <= rowi_ or len(grid_[0]) <= coli_


def check_if_part_number(grid_, rowi_, coli_):
    for rowd, cold in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        row_new, col_new = rowi_ + rowd, coli_ + cold
        if is_oob(grid_, row_new, col_new):
            continue
        if grid_[row_new][col_new] in special_symbols:
            return True
    return False


numbers = []
acc_number = ''
part_number = False
for rowi in range(len(grid)):
    for coli in range(len(grid[0])):
        val = grid[rowi][coli]

        if val.isnumeric():
            acc_number += grid[rowi][coli]
            if check_if_part_number(grid, rowi, coli):
                part_number = True

            is_end = is_oob(grid, rowi, coli + 1) or not grid[rowi][coli + 1].isnumeric()
            if is_end:
                if part_number and acc_number:
                    numbers.append(int(acc_number))

                # reset
                acc_number = ''
                part_number = False

numbers_total = sum(numbers)
print(f'Part 1: {numbers_total}')