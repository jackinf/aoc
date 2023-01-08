from collections import defaultdict
from pprint import pprint

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        lines = [line.split('-') for line in lines]

    connections = defaultdict(list)
    for start, end in lines:
        connections[start].append(end)
        connections[end].append(start)

    paths = []
    q = [('start', set(), ['start'])]
    while q:
        curr, visited, path = q.pop(0)

        if curr == "end":
            paths.append(path)
            continue

        # visit small caves only once
        if curr.islower():
            if curr in visited:
                continue
            visited.add(curr)

        for nei in connections[curr]:
            q.append((nei, visited.copy(), path + [nei]))

    # pprint(paths)
    print(f'Result 1: {len(paths)}')
