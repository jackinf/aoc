import heapq
from collections import defaultdict
from typing import Set

with open('sample.txt') as f:
    blocks_raw = f.read().split('\n\n')

LIMIT = 100
A_COST = 3
B_COST = 1
DEBUG = True


# debug printer
def pr(output, *args, **kwargs):
    if DEBUG:
        print(output, args, kwargs)


# doesn't work
def find_candidates(a_button_steps: int, b_button_steps: int, target_steps: int) -> Set[int]:
    # naive approach
    q = [(0, 0, 0)]  # acc_price, presses, steps
    cache = defaultdict(lambda: float('inf'))
    candidates = set()

    # loop till the whole queue is exhausted
    while q:
        q_len = len(q)
        # print(q_len, end='\r')
        tokens, presses, steps = heapq.heappop(q)
        tokens *= -1  # unpack from heapq
        print(f'{tokens} {presses} {steps}')

        # check if we have hit the limit
        if presses > LIMIT:
            continue

        # if the current price is already higher, we can't hit the target anymore
        if steps > target_steps:
            continue

        # stop condition
        if tokens == target_steps:
            candidates.add(steps)
            continue

        # optimization: is the pair of presses & steps has already been seen with lower price?
        cache_key = (presses, steps)
        if cache[cache_key] < tokens:
            continue
        cache[cache_key] = tokens

        # try out different variations
        tokens *= -1  # prepare for heapq
        heapq.heappush(q, (tokens - A_COST, presses + 1, steps + a_button_steps))
        heapq.heappush(q, (tokens - B_COST, presses + 1, steps + b_button_steps))

    return candidates


final_result = 0
for block_index, block_raw in enumerate(blocks_raw):
    pr(f'BLOCK {block_index}')

    lines = block_raw.split('\n')
    a_xy = lines[0].split(':')[1]
    b_xy = lines[1].split(':')[1]
    pr_xy = lines[2].split(':')[1]

    ax, ay = [int(val[3:]) for val in a_xy.split(',')]
    bx, by = [int(val[3:]) for val in b_xy.split(',')]
    prx, pry = [int(val[3:]) for val in pr_xy.split(',')]

    pr(ax, bx, prx)
    pr(ay, by, pry)
    x_candidates = find_candidates(ax, bx, prx)
    pr(x_candidates)
    y_candidates = find_candidates(ay, by, pry)
    pr(y_candidates)

    common = sorted(list(x_candidates & y_candidates))
    if len(common) > 0:
        result = common[0]
        final_result += result
        pr(f'Found {result}')
    else:
        pr('No matches found')

    pr('')

print(f'Part 1: {final_result}')