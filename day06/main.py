from collections import Counter

if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.read().strip()

    counter = Counter()

    for i, char in enumerate(line):
        counter[char] += 1
        if i >= 4:
            counter[line[i - 4]] -= 1
            if counter[line[i - 4]] == 0:
                del counter[line[i - 4]]

        if len(counter) == 4:
            print(f"Result 1: {i + 1}")
            break

