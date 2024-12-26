import sys

NUM_BLINKS = 75

# someone else's solution. i cheated this day.

def update_stone(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        return [int(stone[:len(stone)//2]), int(stone[len(stone)//2:])]
    return [stone * 2024]


def update(arrangement):
    new_arrangement = {}
    for stone in arrangement.keys():
        new_stones = update_stone(stone)
        for new_stone in new_stones:
            if new_arrangement.get(new_stone) is None:
                new_arrangement[new_stone] = 0
            new_arrangement[new_stone] += arrangement[stone]
    return new_arrangement


if __name__ == '__main__':
    with open('input.txt') as f:
        arrangement = {i: 1 for i in map(int, f.read().split())}

    for _ in range(NUM_BLINKS):
        arrangement = update(arrangement)

    print(f'Number of stones after {NUM_BLINKS} blinks: '
          f'{sum(arrangement.values())}')