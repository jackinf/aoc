with open('sample.txt') as f:
    blocks_raw = f.read().split('\n\n')

A_COST = 3
B_COST = 1
DEBUG = False
BONUS = 10000000000000


# debug printer
def pr(output, *args, **kwargs):
    if DEBUG:
        print(output, *args, **kwargs)


def find_candidates(steps_per_a_press, steps_per_b_press, target_steps, a_press_cost, b_press_cost):
    # make sure that A > B
    if steps_per_a_press < steps_per_b_press:
        return find_candidates(steps_per_b_press, steps_per_a_press, target_steps, b_press_cost, a_press_cost)

    max_a_button_presses = target_steps // steps_per_a_press
    candidates = set()

    # going from higher to lower makes sure that the result tokens are going from lower to higher
    for a_presses in range(max_a_button_presses, -1, -1):
        a_steps = a_presses * steps_per_a_press
        remainder_steps = target_steps - a_steps
        b_presses_div_remainder = remainder_steps % steps_per_b_press

        if b_presses_div_remainder == 0:
            b_presses = remainder_steps // steps_per_b_press
            tokens = a_presses * a_press_cost + b_presses * b_press_cost
            pr(f'found! A presses={a_presses} B presses={b_presses} tokens={tokens}')

            if a_press_cost == A_COST and b_press_cost == B_COST:
                candidates.add((a_presses, b_presses))
            else:
                candidates.add((b_presses, a_presses))

    return candidates


final_result = 0
for block_index, block_raw in enumerate(blocks_raw):
    pr(f'BLOCK {block_index + 1}')

    lines = block_raw.split('\n')
    a_xy = lines[0].split(':')[1]
    b_xy = lines[1].split(':')[1]
    pr_xy = lines[2].split(':')[1]

    ax, ay = [int(val[3:]) for val in a_xy.split(',')]
    bx, by = [int(val[3:]) for val in b_xy.split(',')]
    prx, pry = [int(val[3:]) + BONUS for val in pr_xy.split(',')]

    x_candidates = find_candidates(ax, bx, prx, A_COST, B_COST)
    y_candidates = find_candidates(ay, by, pry, A_COST, B_COST)

    common = sorted(list(x_candidates & y_candidates))
    if len(common) > 0:
        a_presses, b_presses = common[0]
        result = a_presses * A_COST + b_presses * B_COST
        final_result += result
        pr(f'Found {result}')
    else:
        pr('No matches found')


print(f'Part 2: {final_result}')