with open('input.txt') as f:
    text_groups = f.read().split('\n\n')

dirs = [0 if x == 'L' else 1 for x in text_groups[0]]

navmap = {}
for line in text_groups[1].split('\n'):
    key, val = line.split('=')
    left, right = val.replace('(', '').replace(')', '').split(',')
    navmap[key.strip()] = (left.strip(), right.strip())

print(dirs)
print(navmap)

dir_i, steps, curr = 0, 0, 'AAA'
while curr != 'ZZZ':
    dir = dirs[dir_i]
    dir_i += 1
    dir_i %= len(dirs)
    curr = navmap[curr][dir]
    steps += 1

print(f'Part 1: {steps}')