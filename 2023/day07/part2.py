from collections import Counter

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def card_to_num(val: str):
    match val:
        case 'T': return 10
        case 'J': return 1
        case 'Q': return 12
        case 'K': return 13
        case 'A': return 14
        case _: return int(val)

def get_kind(hand: str):
    counter = Counter(hand)
    if hand == 'JJJJJ':
        return FIVE_OF_A_KIND

    most_common_card = Counter(hand.replace('J', '')).most_common()[0][0]
    counter[most_common_card] += counter['J']
    del counter['J']

    counts = sorted(list(counter.values()), reverse=True)
    if counts[0] == 5:
        return FIVE_OF_A_KIND
    if counts[0] == 4 and counts[1] == 1:
        return FOUR_OF_A_KIND
    if counts[0] == 3 and counts[1] == 2:
        return FULL_HOUSE
    if counts[0] == 3 and counts[1] == 1 and counts[2] == 1:
        return THREE_OF_A_KIND
    if counts[0] == 2 and counts[1] == 2 and counts[2] == 1:
        return TWO_PAIR
    if counts[0] == 2 and counts[1] == counts[2] == counts[3] == 1:
        return ONE_PAIR
    return HIGH_CARD


with open('input.txt', 'r') as f:
    lines = [[x[0], int(x[1])] for x in [line.split() for line in f.read().split('\n')]]

lines.sort(key=lambda x: x[0], reverse=True)
lines = [[[card_to_num(val) for val in list(x[0])], int(x[1]), get_kind(x[0])] for x in lines]
lines.sort(key=lambda x: (x[2], x[0]))
scores = [x[1] * (i + 1) for i, x in enumerate(lines)]
total_score = sum(scores)

print(f'Part 2: {total_score}')

