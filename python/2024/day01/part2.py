from collections import Counter


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
similarity_scores = Counter(rights)

N = len(lefts)

final_result = 0
for i in range(N):
    result = lefts[i] * similarity_scores[lefts[i]]
    final_result += result

print(f'Part 2: {final_result}')
