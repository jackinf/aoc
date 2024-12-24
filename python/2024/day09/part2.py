from collections import defaultdict

def read_input_file(file_path):
    with open(file_path) as f:
        return f.read()

def parse_line(line):
    spaces = defaultdict(int)
    files = defaultdict(int)
    index = 0
    id = -1

    while index < len(line):
        id += 1
        files[id] = int(line[index])
        index += 1

        if index < len(line):
            spaces[id] = int(line[index])
            index += 1

    # Add initial space block
    # spaces[-1] = 0
    return files, spaces

def step(files, spaces, results) -> bool:
    for file_id in sorted(files.keys(), reverse=True):
        for spaces_id in sorted(spaces.keys(), reverse=False):
            # print(f'Spaces id: {spaces_id}, File id: {file_id}')
            if files[file_id] <= spaces[spaces_id]:
                # print(f'File {file_id} moved into {spaces_id}')
                spaces[spaces_id] -= files[file_id]
                results[spaces_id].append((file_id, files[file_id]))

                del files[file_id]
                # if spaces[spaces_id] == 0:
                #     del spaces[spaces_id]

                return False

    return True

def solve(files, spaces):
    results = defaultdict(list)
    files2 = files.copy()
    spaces2 = spaces.copy()

    while files and spaces:
        done = step(files, spaces, results)

        if done:
            break

    result_str = ''
    for file_id in sorted(files2.keys(), reverse=False):
        if file_id in files:
            result_str += (str(file_id) * files[file_id])
        else:
            result_str += ('.' * files2[file_id])

        occupied_spaces = 0
        for k, v in results[file_id]:
            result_str = result_str + (str(k) * v)
            occupied_spaces += v

        left_spaces = spaces2[file_id] - occupied_spaces
        result_str += '.' * left_spaces

    return result_str

def calculate_final_result(result):
    final_result = sum((0 if k == '.' else int(k)) * i for i, k in enumerate(result))
    return final_result

def main():
    # Change the file path as needed
    file_path = 'input.txt'
    line = read_input_file(file_path)

    files, spaces = parse_line(line)
    result = solve(files, spaces)

    print(result)

    final_result = calculate_final_result(result)
    print(f'Part 2: {final_result}')

if __name__ == "__main__":
    main()

# 95174136247 - too low