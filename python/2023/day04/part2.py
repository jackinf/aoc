with open('input.txt') as f:
    lines = f.read().split('\n')

cards = [1] * len(lines)
for card_index, line in enumerate(lines):
    winning, owned = line.split(':')[1].split('|')
    matches = len(set(winning.split()) & set(owned.split()))
    for score_index in range(1, matches + 1):
        cards[card_index + score_index] += cards[card_index]

total = sum(cards)
print(f'Part 2: {total}')