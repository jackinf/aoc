def read_input(file_name: str):
    with open(file_name) as f:
        blocks_raw = f.read().split('\n\n')

    for block_index, block_raw in enumerate(blocks_raw):
        lines = block_raw.split('\n')
        a_xy = lines[0].split(':')[1]
        b_xy = lines[1].split(':')[1]
        pr_xy = lines[2].split(':')[1]

        ax, ay = [int(val[3:]) for val in a_xy.split(',')]
        bx, by = [int(val[3:]) for val in b_xy.split(',')]
        prx, pry = [int(val[3:]) for val in pr_xy.split(',')]

        BONUS = 10000000000000
        yield ax, ay, bx, by, prx + BONUS, pry + BONUS

"""
- a_x * a + b_x * b = x_prize
- a_y * a + b_y * b = y_prize
"""
def find_intersection(
    a_x: int, a_y: int, b_x: int, b_y: int, x_prize: int, y_prize: int
) -> tuple[float, float]:
    a_x_with_b_y = a_x * b_y
    x_prize_with_b_y = x_prize * b_y
    a_y_with_b_x = a_y * b_x
    y_prize_with_b_x = y_prize * b_x
    a = (x_prize_with_b_y - y_prize_with_b_x) / (a_x_with_b_y - a_y_with_b_x)
    b = (y_prize - a_y * a) / b_y
    return a, b

def solve(blocks):
    total = 0
    for block in blocks:
        a, b = find_intersection(*block)
        if a.is_integer() and b.is_integer():
            total += a * 3 + b
    return total

def run():
    blocks = list(read_input('input.txt'))
    print(blocks)

    final_result = solve(blocks)
    print(f'Part 2: {final_result}')  # 47954945384809 vs 77407675412647

if __name__ == '__main__':
    run()