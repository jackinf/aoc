with open('input.txt') as f:
    lines = f.read().split('\n')

total = sum(2 ** (matches - 1) for matches in [len(set(cards[0]) & set(cards[1])) for cards in [[cards.split() for cards in line.split(':')[1].split('|')] for line in lines]] if matches > 0)
print(f'Part 1: {total}')
