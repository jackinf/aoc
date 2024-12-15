# with open('python/2024/day11/sample.txt') as f:
    # content = f.read()
content = '1'
# content = '0 1 10 99 999'
# content = '77 515 6779622 6 91370 959685 0 9861'
stones = list(map(int, content.split()))

for i in range(75):
    tmp = []

    for stone in stones:
        stone_str = str(stone)
        N = len(stone_str)

        if stone == 0:
            tmp.append(1)
        elif N % 2 == 0:
            left, right = stone_str[:N//2], stone_str[N//2:]
            tmp.append(int(left))
            tmp.append(int(right))
        else:
            tmp.append(stone * 2024)

    stones = tmp
    print(i, len(stones))

print(f'Part 2: {len(stones)}')