from collections import defaultdict


# with open('python/2024/day09/input.txt') as f:
with open('python/2024/day09/sample.txt') as f:
    line = f.read()

# 2333133121414131402
# 00...111...2...333.44.5555.6666.777.888899
id = -1

# line = '12345'
spaces = defaultdict(int)
files = defaultdict(int)

index = 0
while index < len(line):
    id += 1
    files[id] = int(line[index])
    index += 1

    if index < len(line):
        spaces[id] = int(line[index])
        index += 1

# print('files', files)
# print('spaces', spaces)

# start with file block
spaces[-1] = 0

result = []
old_id = id

files_pointer = old_id
N = old_id
id = -1


while id < files_pointer:
    print(id, files_pointer, files, spaces)

    if files[files_pointer] == 0:
        # print(files)
        # del files[files_pointer]
        files_pointer -= 1
        continue

    if spaces[id] == 0:
        # del spaces[id]
        id += 1
        for _ in range(files[id]):
            result.append(id)
        continue

    if files[files_pointer] <= spaces[id]:
        diff = spaces[id] - files[files_pointer]
        print(diff)
        files[files_pointer] -= diff
        spaces[id] -= diff

        for _ in range(diff):
            result.append(files_pointer)

        files_pointer = N
        continue

    files_pointer -= 1

# 022111222
print(result)

final_result = 0
for i, val in enumerate(result):
    final_result += i * val

print(f'Part 2: {final_result}')
    
    
# 6283404590840