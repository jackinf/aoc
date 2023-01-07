from collections import Counter

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        lines = [line.split('->') for line in lines]
        lines = [(item[0].split(','), item[1].split(',')) for item in lines]
        lines = [[(int(item[0][0]), int(item[0][1])), (int(item[1][0]), int(item[1][1]))] for item in lines]

    counter = Counter()

    for start, end in lines:
        hdir = 1 if start[0] < end[0] else 0 if start[0] == end[0] else -1
        vdir = 1 if start[1] < end[1] else 0 if start[1] == end[1] else -1

        curr = [start[0], start[1]]
        while True:
            tcurr = tuple(curr)
            counter[tcurr] += 1
            curr[0] += hdir
            curr[1] += vdir

            if tcurr == end:
                break

    res = sum(1 for count in counter.values() if count > 1)
    print(f'Result 2: {res}')
