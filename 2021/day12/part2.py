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

    small_caves = {cave:1 for cave in connections.keys() if cave.islower() and cave != "start" and cave != "end"}

    paths = set()
    for cave in small_caves.keys():
        allowed_visits_start = small_caves.copy()
        allowed_visits_start[cave] += 1
        print(allowed_visits_start)

        q = [('start', allowed_visits_start, ['start'])]
        while q:
            curr, allowed_visits, path = q.pop(0)

            if curr == "end":
                paths.add(','.join(path))
                continue

            # visit small caves only once
            if curr.islower() and curr != 'start':
                if allowed_visits[curr] == 0:
                    continue
                allowed_visits[curr] -= 1

            for nei in connections[curr]:
                if nei == 'start':
                    continue
                q.append((nei, allowed_visits.copy(), path + [nei]))

    # pprint(paths)
    print(f'Result 2: {len(paths)}')
