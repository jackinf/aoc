with open('input.txt') as f:
    lines = f.read().split('\n')

cards = [1] * len(lines)
for card_index, line in enumerate(lines):
    split_line = line.split(':')
    cards_both = split_line[1].split('|')
    cards_winning = set(cards_both[0].split())
    cards_attempt = set(cards_both[1].split())
    matches = len(cards_winning & cards_attempt)
    for score_index in range(1, matches + 1):
        cards[card_index + score_index] += cards[card_index]

total = sum(cards)
print(f'Part 2: {total}')