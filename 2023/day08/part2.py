import math
from collections import defaultdict

with open('input.txt') as f:
    text_groups = f.read().split('\n\n')

dirs = [0 if x == 'L' else 1 for x in text_groups[0]]

navmap = {}
for line in text_groups[1].split('\n'):
    key, val = line.split('=')
    left, right = val.replace('(', '').replace(')', '').split(',')
    navmap[key.strip()] = (left.strip(), right.strip())

ghosts = [x for x in navmap.keys() if x[2] == 'A']

dir_i, steps = 0, 0
loop_cache = defaultdict(list)
for ghost in ghosts:
    curr = ghost
    while True:
        steps += 1

        dir = dirs[dir_i]
        dir_i += 1
        dir_i %= len(dirs)

        curr = navmap[curr][dir]
        if curr[2] == 'Z':
            loop_cache[(ghost, dir_i, curr)].append(steps)

        # are we in a loop? have we seen same position twice already?
        if len(loop_cache[(ghost, dir_i, curr)]) == 2:
            break

loop_cache = {i: x for i, x in loop_cache.items() if len(x) > 0}
ghost_step_map = {key[0]: (val[0], val[1] - val[0]) for key, val in loop_cache.items()}
res = math.lcm(*[val[1] - val[0] for val in loop_cache.values()])
print(f'Part 2: {res}')
