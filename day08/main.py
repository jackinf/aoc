def mark_edges_visible(visibles):
    for i in range(len(visibles)):
        visibles[i][0] = True
        visibles[i][-1] = True

    for j in range(len(visibles[0])):
        visibles[0][j] = True
        visibles[-1][j] = True

def calculate_maxes(grid):
    leftmax = [row[:] for row in grid[:]]
    rightmax = [row[:] for row in grid[:]]
    topmax = [row[:] for row in grid[:]]
    bottommax = [row[:] for row in grid[:]]

    for row in range(len(leftmax)):
        for col in range(1, len(leftmax[0])):
            leftmax[row][col] = max(leftmax[row][col], leftmax[row][col - 1])

    for row in range(len(rightmax)):
        for col in range(len(rightmax[0]) - 2, -1, -1):
            rightmax[row][col] = max(rightmax[row][col], rightmax[row][col + 1])

    for col in range(len(topmax)):
        for row in range(1, len(topmax)):
            topmax[row][col] = max(topmax[row][col], topmax[row - 1][col])

    for col in range(len(bottommax)):
        for row in range(len(bottommax) - 2, -1, -1):
            bottommax[row][col] = max(bottommax[row][col], bottommax[row + 1][col])

    return leftmax, rightmax, topmax, bottommax


def calculate_visibles(visibles, grid, leftmax, rightmax, topmax, bottommax):
    visibles = [x[:] for x in visibles[:]]
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            visible_from_left = leftmax[row][col - 1] < grid[row][col]
            visible_from_right = rightmax[row][col + 1] < grid[row][col]
            visible_from_top = topmax[row - 1][col] < grid[row][col]
            visible_from_bottom = bottommax[row + 1][col] < grid[row][col]

            visibles[row][col] = visible_from_left or visible_from_right or visible_from_top or visible_from_bottom

    return visibles

def bruteforce_best_position(grid):
    best_score = 1
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            score = 1
            for row2 in range(row + 1, len(grid)):
                if grid[row2][col] >= grid[row][col]:
                    break
            score *= abs(row2 - row)

            for row2 in range(row - 1, -1, -1):
                if grid[row2][col] >= grid[row][col]:
                    break
            score *= abs(row2 - row)

            for col2 in range(col + 1, len(grid[0])):
                if grid[row][col2] >= grid[row][col]:
                    break
            score *= abs(col2 - col)

            for col2 in range(col - 1, -1, -1):
                if grid[row][col2] >= grid[row][col]:
                    break
            score *= abs(col2 - col)

            best_score = max(score, best_score)

    return best_score

if __name__ == '__main__':
    with open('input.txt') as f:
        grid = [[int(x) for x in list(line.strip())] for line in f]
    visibles = [[False for x in row] for row in grid]

    mark_edges_visible(visibles)
    leftmax, rightmax, topmax, bottommax = calculate_maxes(grid)
    visibles = calculate_visibles(visibles, grid, leftmax, rightmax, topmax, bottommax)
    total_visible = sum(x for y in visibles for x in y if x)

    print(f'Result 1: {total_visible}')

    best_score = bruteforce_best_position(grid)

    print(f'Result 2: {best_score}')
