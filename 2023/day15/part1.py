with open('input.txt', 'r') as f:
    code = f.readline().split(",")

results = []
for item in code:
    curr = 0
    for ch in item:
        curr += ord(ch)
        curr *= 17
        curr %= 256
    results.append(curr)

print(f'Part 1: {sum(results)}')