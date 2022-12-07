from collections import defaultdict
from typing import List


def parse(lines: List[str]):
    disk = {}
    path = []
    p = 0
    while p < len(lines):
        line = lines[p].split()
        p += 1

        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    continue
                elif line[2] == "..":
                    if path:
                        path.pop()
                else:
                    path.append(line[2])

            elif line[1] == "ls":
                while p < len(lines):
                    line = lines[p].split()
                    p += 1

                    if line[0] == "$":
                        p -= 1
                        break
                    elif line[0] == "dir":
                        fullpath = "/".join([''] + path + [line[1]]) + "/"
                        disk[fullpath] = disk.get(fullpath, [])
                    else:
                        fullpath = "/".join([''] + path + [line[1]])
                        disk[fullpath] = int(line[0])

    return disk


def calculate_folder_sizes(disk):
    files_only = {k:v for k,v in disk.items() if k[-1] != "/"}

    folder_sizes = defaultdict(int)
    for filename, filesize in files_only.items():
        path = filename.split('/')[1:]
        while path:
            path.pop()
            fullpath = '/'.join(path)
            folder_sizes[fullpath] += filesize

    return folder_sizes


def filter_folders_by_size(folder_sizes):
    return {k:v for k,v in folder_sizes.items() if v <= 100_000}


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    disk = parse(lines)
    folder_sizes = calculate_folder_sizes(disk)
    filtered_folder_sizes = filter_folders_by_size(folder_sizes)
    result1 = sum(v for k,v in filtered_folder_sizes.items())

    print(f'Result 1: {result1}')

    total_space = 70_000_000
    req_unused_space = 30_000_000
    curr_unused_space = total_space - folder_sizes['']
    to_free_up = req_unused_space - curr_unused_space

    for dir, size in sorted(folder_sizes.items(), key=lambda x: x[1]):
        if size > to_free_up:
            print(f'Result 2: {dir}, {size}')
            break
