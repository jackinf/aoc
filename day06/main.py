from collections import Counter


def find_unique_seq_i(data: str, seq_len: int):
    counter = Counter()
    for i, char in enumerate(data):
        counter[char] += 1
        if i >= seq_len:
            counter[data[i - seq_len]] -= 1
            if counter[data[i - seq_len]] == 0:
                del counter[data[i - seq_len]]

        if len(counter) == seq_len:
            return i + 1
    return -1


if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.read().strip()

    print(f"Result 1: {find_unique_seq_i(line, 4)}")
    print(f"Result 2: {find_unique_seq_i(line, 14)}")
