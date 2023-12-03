with open('input.txt') as f:
    whole_text = f.read()
    grid = [list(line) for line in whole_text.split('\n')]


def is_oob(rowi_, coli_):
    return rowi_ < 0 or coli_ < 0 or len(grid) <= rowi_ or len(grid[0]) <= coli_


def find_left(i, j):
    if not is_oob(i, j) and grid[i][j].isnumeric():
        return find_left(i, j - 1)
    return j + 1


def collect_number(i, j, acc, seen):
    if (i, j) in seen:
        return
    seen.add((i, j))

    if not is_oob(i, j) and grid[i][j].isnumeric():
        acc.append(grid[i][j])
        collect_number(i, j + 1, acc, seen)


# finding gear coordinates
stars = {(rowi, coli) for coli in range(len(grid[0])) for rowi in range(len(grid)) if grid[rowi][coli] == '*'}

seen = set()
products = []
for i, j in stars:
    collected = []
    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        ni, nj = i + di, j + dj
        if is_oob(ni, nj) or not grid[ni][nj].isnumeric():
            continue

        startj = find_left(ni, nj)
        acc = []
        collect_number(ni, startj, acc, seen)
        if acc:
            collected.append(int(''.join(acc)))
    if len(collected) == 2:
        products.append(collected[0] * collected[1])

products_total = sum(products)
print(f'Part 2: {products_total}')

