with open('input.txt') as f:
    grid = f.read().split('\n')

# column transposition
column_transposed = [''.join(row[i] for row in grid) for i in range(len(grid[0]))]

ROWS = len(grid)
diagonal_transposed = []
reverse_diagonal_transposed = []

for d in range(2 * ROWS - 1):
    diagonal = []
    reverse_diagonal = []
    for row_index in range(ROWS):
        # diagonal transposition
        col_index = d - row_index
        if 0 <= col_index < ROWS:
            diagonal.append(grid[row_index][col_index])

        # reverse diagonal transposition
        col_index = d - (ROWS - 1 - row_index)
        if 0 <= col_index < ROWS:
            reverse_diagonal.append(grid[row_index][col_index])

    diagonal_transposed.append(''.join(diagonal))
    reverse_diagonal_transposed.append(''.join(reverse_diagonal))

#
# Counting
#

found_count = 0
xmas = 'XMAS'
samx = 'SAMX'

# count rows
for row_index in range(len(grid)):
    found_count += grid[row_index].count(xmas)
    found_count += grid[row_index].count(samx)

# count columns
for row_index in range(len(column_transposed)):
    found_count += column_transposed[row_index].count(xmas)
    found_count += column_transposed[row_index].count(samx)

# count diagonals
for row_index in range(len(diagonal_transposed)):
    found_count += diagonal_transposed[row_index].count(xmas)
    found_count += diagonal_transposed[row_index].count(samx)

# count reversed diagonals
for row_index in range(len(reverse_diagonal_transposed)):
    found_count += reverse_diagonal_transposed[row_index].count(xmas)
    found_count += reverse_diagonal_transposed[row_index].count(samx)

print(f'Part 1: {found_count}')