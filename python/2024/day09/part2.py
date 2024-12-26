from typing import List

DEBUG = False


def read_input_file(file_path):
    with open(file_path) as f:
        return f.read()

def parse_line(line):
    file_id = 0
    arr = []
    index = 0

    while index < len(line):
        # for _ in range(int(line[index])):
        arr.append([file_id, int(line[index])])
        index += 1

        if index >= len(line):
            break

        # for _ in range(int(line[index])):
        arr.append([None, int(line[index])])
        index += 1

        file_id += 1

    return arr

def max_id(data: list):
    return max(map(lambda x: x[0], filter(lambda x: x[0] is not None, data)))

def find_pos(data, id):
    return next(i for i, v in enumerate(data) if v[0] == id)

def subst(arr, p1, p2):
    file, space = arr[p1], arr[p2]
    diff = file[1] - space[1]

    if diff < 0:
        arr[p2] = (file[0], file[1])
        arr[p1] = (None, arr[p1][1])
        arr.insert(p2 + 1, (None, abs(diff)))
    elif diff == 0:
        arr[p2] = (file[0], file[1])
        arr[p1] = (None, arr[p1][1])

def solve(data: List[List[int | None]]):
    curr_id = max_id(data)

    while curr_id > 0:
        p1 = find_pos(data, curr_id)

        for p2, _ in filter(lambda x: x[1][0] is None and x[0] < p1, enumerate(data)):
            if data[p2][1] >= data[p1][1]:
                subst(data, p1, p2)
                break

        curr_id -= 1

    res = []
    for k, v in data:
        key = 0 if k is None else k
        for _ in range(v):
            res.append(key)
    return sum([i * v for i,v in enumerate(res)])


def main():
    # Change the file path as needed
    file_path = 'input.txt'
    line = read_input_file(file_path)

    arr = parse_line(line)
    if DEBUG:
        print(arr)
    res = solve(arr)
    print(f'Part 2: {res}')


if __name__ == "__main__":
    main()
