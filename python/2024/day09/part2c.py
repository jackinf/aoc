from typing import List


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

def solve(arr):
    pass


def main():
    # Change the file path as needed
    file_path = 'sample.txt'
    line = read_input_file(file_path)

    arr = parse_line(line)
    print(arr)
    solve(arr)


if __name__ == "__main__":
    main()