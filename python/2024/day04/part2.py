with open('input.txt') as f:
    grid = f.read().split('\n')

found_count = 0
for i in range(len(grid) - 2):
    for j in range(len(grid[0]) - 2):
        c00, c02, c11, c20, c22 = grid[i][j], grid[i][j+2], grid[i+1][j+1], grid[i+2][j], grid[i+2][j+2]

        if c11 != 'A':
            continue

        case1 = c00 == 'M' and c02 == 'M' and c20 == 'S' and c22 == 'S'
        case2 = c00 == 'M' and c02 == 'S' and c20 == 'M' and c22 == 'S'
        case3 = c00 == 'S' and c02 == 'M' and c20 == 'S' and c22 == 'M'
        case4 = c00 == 'S' and c02 == 'S' and c20 == 'M' and c22 == 'M'

        if case1 or case2 or case3 or case4:
            found_count += 1

print(f'Part 2: {found_count}')