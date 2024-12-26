# with open('python/2024/day11/sample.txt') as f:
    # content = f.read()
content = '1'
# content = '0 1 10 99 999'
# content = '77 515 6779622 6 91370 959685 0 9861'
stones = list(map(int, content.split()))

def next_stones(stone):
    if stone == 0:
        return [1]

    stone_str, N = str(stone), len(str(stone))
    if N % 2 == 0:
        return [int(stone_str[:N//2]), int(stone_str[N//2:])]

    return [stone * 2024]

def next_state(arrangement):
    new_arrangement = {}
    for stone in arrangement.keys():
        new_stones = next_stones(stone)
        for new_stone in new_stones:
            if new_arrangement.get(new_stone) is None:
                new_arrangement[new_stone] = 0
            new_arrangement[new_stone] += arrangement[stone]
    return new_arrangement


def run():
    with open('input.txt') as f:
        stones = {i: 1 for i in map(int, f.read().split())}

    for _ in range(75):
        stones = next_state(stones)

    print(f'Part 2: {sum(stones.values())}')

if __name__ == '__main__':
    run()

# 223767210249237
