ROCK = "A"
PAPER = "B"
SCISSORS = "C"

# P2's hand's translation to P1's hand
hand_translations = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

# for 1st (and 2nd) solution - rulebook
VICT = 6
DRAW = 3
LOSS = 0
scores = {
    (ROCK, ROCK): 1 + DRAW,
    (ROCK, PAPER): 1 + LOSS,
    (ROCK, SCISSORS): 1 + VICT,
    (PAPER, ROCK): 2 + VICT,
    (PAPER, PAPER): 2 + DRAW,
    (PAPER, SCISSORS): 2 + LOSS,
    (SCISSORS, ROCK): 3 + LOSS,
    (SCISSORS, PAPER): 3 + VICT,
    (SCISSORS, SCISSORS): 3 + DRAW,
}

# for 2nd solution - P1's hand + what needs to happen = P2's hand
NEED_TO_LOSE = "X"
NEED_TO_DRAW = "Y"
NEED_TO_WIN = "Z"
reversed_hands = {
    (ROCK, NEED_TO_LOSE): SCISSORS,
    (ROCK, NEED_TO_DRAW): ROCK,
    (ROCK, NEED_TO_WIN): PAPER,
    (PAPER, NEED_TO_LOSE): ROCK,
    (PAPER, NEED_TO_DRAW): PAPER,
    (PAPER, NEED_TO_WIN): SCISSORS,
    (SCISSORS, NEED_TO_LOSE): PAPER,
    (SCISSORS, NEED_TO_DRAW): SCISSORS,
    (SCISSORS, NEED_TO_WIN): ROCK,
}


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = [tuple(line.split(' ')) for line in f.read().split('\n')]

    result1_me = 0
    for line in lines:
        result1_me += scores[(hand_translations[line[1]], line[0])]

    print(f'Result 1: {result1_me}')

    result2_me = 0
    for line in lines:
        hand = reversed_hands[(line[0], line[1])]
        score = scores[(hand, line[0])]
        result2_me += score

    print(f'Result 2: {result2_me}')
