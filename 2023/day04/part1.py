with open('input.txt') as f:
    lines = f.read().split('\n')

total = 0
for line in lines:
    cards_both = line.split(':')[1].split('|')
    cards_winning = set(cards_both[0].split())
    cards_attempt = set(cards_both[1].split())
    matches = len(cards_winning & cards_attempt)
    score = 2 ** (matches - 1) if matches > 0 else 0
    total += score

print(f'Part 1: {total}')