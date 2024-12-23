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
    return files, spaces, id

def work(files, spaces, results) -> bool:
    for file_id in sorted(files.keys(), reverse=True):
        for spaces_id in sorted(spaces.keys(), reverse=False):
            # print(f'Spaces id: {spaces_id}, File id: {file_id}')
            if files[file_id] <= spaces[spaces_id]:
                print(f'File {file_id} moved into {spaces_id}')
                spaces[spaces_id] -= files[file_id]
                results[spaces_id].append((file_id, files[file_id]))

                del files[file_id]
                # if spaces[spaces_id] == 0:
                #     del spaces[spaces_id]

                return False

    return True

def process_files_and_spaces(files, spaces, last_id):
    results = defaultdict(list)
    # files_pointer = last_id
    # id = -1
    # N = last_id

    # spaces_id = 0
    # files_id = 0

    files2 = files.copy()

    while files and spaces:
        done = work(files, spaces, results)

        if done:
            break

    result_str = ''

    # files2: defaultdict(<class 'int'>, {0: 2, 1: 3, 2: 1, 3: 3, 4: 2, 5: 4, 6: 4, 7: 3, 8: 4, 9: 2})
    # results: @defaultdict(<class 'list'>, {0: [(9, 2), (2, 1)], 1: [(7, 3)], 2: [(4, 2)]})

    for file_id in sorted(files.keys(), reverse=False):
        result_str = result_str + (str(file_id) * files2[file_id])

        for k, v in results[file_id]:
            result_str = result_str + (str(k) * v)

    return result_str

def calculate_final_result(result):
    final_result = sum(i * val for i, val in enumerate(result))
    return final_result

def main():
    # Change the file path as needed
    file_path = 'sample.txt'
    line = read_input_file(file_path)

    files, spaces, last_id = parse_line(line)
    result = process_files_and_spaces(files, spaces, last_id)

    print(result)

    final_result = calculate_final_result(result)
    print(f'Part 2: {final_result}')

if __name__ == "__main__":
    main()
