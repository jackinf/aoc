with open('input.txt') as f:
    lines = f.read().split('\n')

lefts = []
rights = []
for line in lines:
    left, right = line.split()
    left = int(left)
    right = int(right)
    
    lefts.append(left)
    rights.append(right)

lefts.sort()
rights.sort()

N = len(lefts)
assert len(lefts) == len(rights)

final_result = 0
for i in range(N):
    result = abs(lefts[i] - rights[i])
    final_result += result

print(f'Part 1: {final_result}')
