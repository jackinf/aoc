with open('sample.txt', 'r') as f:
    code = f.readline().split(",")

boxes = [[]] * 256
for item in code:
    op = '-' if item[-1] == '-' else '='
    val, num = item.split(op)

    curr = 0
    for ch in val:
        curr += ord(ch)
        curr *= 17
        curr %= 256

    if op == '=':
        boxes[curr].append((val, num))

    # todo: implement subscraction
    # if op == '-':
    #     boxes = [(a, b) for a, b in boxes if a == val]

print(boxes)
# print(f'Part 2: {sum(results)}')