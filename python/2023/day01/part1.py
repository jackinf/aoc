with open('input.txt') as f:
    lines = [line for line in f.read().split('\n')]

nums = [[x for x in line if x.isnumeric()] for line in lines]
sums = [int(x[0] + x[-1]) for x in nums]
total_sum = sum(sums)

print(f'Part 1: {total_sum}')
