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
    spaces[-1] = 0
    return files, spaces, id

def process_files_and_spaces(files, spaces, last_id):
    result = []
    files_pointer = last_id
    id = -1

    while id < files_pointer:
        if files[files_pointer] == 0:
            del files[files_pointer]
            files_pointer -= 1
            continue

        if spaces[id] == 0:
            del spaces[id]
            id += 1
            for _ in range(files[id]):
                result.append(id)
            continue

        files[files_pointer] -= 1
        spaces[id] -= 1
        result.append(files_pointer)

    return result

def calculate_final_result(result):
    final_result = sum(i * val for i, val in enumerate(result))
    return final_result

def main():
    # Change the file path as needed
    # line = read_input_file('sample.txt')
    line = read_input_file('input.txt')

    files, spaces, last_id = parse_line(line)
    result = process_files_and_spaces(files, spaces, last_id)

    final_result = calculate_final_result(result)
    print(f'Part 1: {final_result}')

if __name__ == "__main__":
    main()
