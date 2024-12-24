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

    return files, spaces

def step(files, spaces, results) -> bool:
    for file_id in sorted(files.keys(), reverse=True):
        for spaces_id in sorted(spaces.keys(), reverse=False):
            if files[file_id] <= spaces[spaces_id]:
                spaces[spaces_id] -= files[file_id]
                results[spaces_id].append((file_id, files[file_id]))

                del files[file_id]

                return False

    return True

def solve(files, spaces):
    results = defaultdict(list) # collect all the movements of the file here

    # as we will modify the arrays (by subtracting or removing values)
    files2 = files.copy()
    spaces2 = spaces.copy()

    while files and spaces:
        done = step(files, spaces, results)

        if done:
            break

    # construct the answer
    result = []
    for file_id in sorted(files2.keys(), reverse=False):
        val = str(file_id) if file_id in files else '.'
        for _ in range(files2[file_id]):
            result.append(val)

        left_spaces = spaces2[file_id]
        for k, v in results[file_id]:
            for _ in range(v):
                result.append(str(k))
            left_spaces -= v

        for _ in range(left_spaces):
            result.append('.')

    return result

def calculate_final_result(result):
    final_result = sum((0 if k == '.' else int(k)) * i for i, k in enumerate(result))
    return final_result

def main():
    file_path = 'sample1.txt'
    line = read_input_file(file_path)

    files, spaces = parse_line(line)
    result = solve(files, spaces)

    print(result)

    final_result = calculate_final_result(result)
    print(f'Part 2: {final_result}')

if __name__ == "__main__":
    main()

# 95174136247 - too low
# 8456900406063 - too high
