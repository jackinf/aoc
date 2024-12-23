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

def calculate_final_result(result):
    final_result = sum(i * val for i, val in enumerate(result))
    return final_result

def solve(arr: List[List[int | None]]):
    in_progress = True
    while in_progress:
        spaces, files = [0], [0]
        for p1 in range(len(arr)):
            p1_key, p1_space = arr[p1]
            index_found = -1
            if p1_key is None:
                for p2 in range(len(arr) - 1, -1, -1):
                    if arr[p2][0] is not None and arr[p2][1] <= arr[p1][1]:
                        index_found = p2
                        break

                if index_found != -1:
                    arr[p1][1] -= arr[index_found][1]
                    arr.insert(p1, [arr[index_found][0], arr[index_found][1]])
                    arr[index_found + 1][0] = None

            if index_found != -1:
                break

        # todo: check if finished
        in_progress = False
        start = 0
        for i in range(len(arr)):
            if arr[i][0] is None:
                start = i
                break

        for j in range(start + 1, len(arr)):
            if arr[j][0] is not None:
                in_progress = True
                break


        print(spaces, files)



def main():
    # Change the file path as needed
    file_path = 'sample.txt'
    line = read_input_file(file_path)

    arr = parse_line(line)
    print(arr)
    solve(arr)


if __name__ == "__main__":
    main()
