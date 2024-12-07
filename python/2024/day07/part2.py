with open('input.txt') as f:
    lines = f.readlines()

final_result = 0
for i, line in enumerate(lines):
    left, right = line.split(':')
    left = int(left)
    right = list(map(int, right.split()))

    q = [(1, right[0])]
    while q:
        right_index, ans = q.pop(0)
        if ans > left:
            continue

        if right_index == len(right):
            if ans == left:
                final_result += ans
                break
            continue

        q.append((right_index + 1, ans + right[right_index]))
        q.append((right_index + 1, ans * right[right_index]))
        q.append((right_index + 1, int(str(ans) + str(right[right_index]))))

print(f'Part 2: {final_result}')