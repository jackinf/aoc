from collections import Counter

if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]
        lines = [line.split('->') for line in lines]
        lines = [(item[0].split(','), item[1].split(',')) for item in lines]
        lines = [[(int(item[0][0]), int(item[0][1])), (int(item[1][0]), int(item[1][1]))] for item in lines]

    counter = Counter()

    horizontals = [item for item in lines if item[0][1] == item[1][1]]
    verticals = [item for item in lines if item[0][0] == item[1][0]]

    for start, end in horizontals:
        start, end = (start, end) if start[0] < end[0] else (end, start)
        for i in range(start[0], end[0] + 1):
            counter[(i, start[1])] += 1

    for start, end in verticals:
        start, end = (start, end) if start[1] < end[1] else (end, start)
        for i in range(start[1], end[1] + 1):
            counter[(start[0], i)] += 1

    res = sum(1 for count in counter.values() if count > 1)
    print(f'Result 1: {res}')
