from typing import List

DEBUG = True


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
    final_result = sum((0 if k == '.' else int(k)) * i for i, k in enumerate(result))
    return final_result

def solve(arr: List[List[int | None]]):
    in_progress = True
    prev_res = ''
    while in_progress:
        for p1 in range(len(arr) - 1, -1, -1):
            space_index_found = -1

            # is it not the space, but file id/value?
            if arr[p1][0] is not None:
                for p2 in range(p1):
                    if arr[p2][0] is None and arr[p2][1] >= arr[p1][1]:
                        space_index_found = p2
                        break

                if space_index_found != -1:
                    key, val = arr[p1]
                    arr[space_index_found][1] -= val
                    arr[p1][0] = None
                    arr.insert(space_index_found, [key, val])

            if space_index_found != -1:
                break

        if DEBUG:
            print(arr)
        res = ''
        for k, v in arr:
            key = '.' if k is None else str(k)
            res += key * v
        if DEBUG:
            print(res)
        if prev_res == res:
            break
        prev_res = res

    if DEBUG:
        print(prev_res)
    if DEBUG:
        print(arr)
    return prev_res


def main():
    # Change the file path as needed
    file_path = 'sample.txt'
    line = read_input_file(file_path)

    arr = parse_line(line)
    if DEBUG:
        print(arr)
    res = solve(arr)
    checksum = calculate_final_result(res)
    print(checksum)


if __name__ == "__main__":
    main()
