with open('input.txt') as f:
    lines = f.read().split('\n')

total = 0
for line in lines:
    winning, owned = line.split(':')[1].split('|')
    matches = len(set(winning.split()) & set(owned.split()))
    total += 2 ** (matches - 1) if matches > 0 else 0

print(f'Part 1: {total}')

# Alternative solution for lolz
total_alternative = sum(2 ** (x - 1) for x in [len(set(cards[0]) & set(cards[1])) for cards in [[cards.split() for cards in line.split(':')[1].split('|')] for line in lines]] if x > 0)
print(f'Part 1 (alternative): {total}')
