from collections import defaultdict, Counter
from pprint import pprint
from typing import Tuple, List, Set


DEBUG = False


def read_input(file_name: str) -> List[Tuple[str, str]]:
    with open(file_name) as f:
        lines = f.read().split('\n')
        return [(line.split('-')[0], line.split('-')[1]) for line in lines]


def run():
    pairs = read_input('input.txt')

    connections = defaultdict(set)
    for left, right in pairs:
        connections[left].add(right)
        connections[right].add(left)

    if DEBUG:
        print(connections)
    triplets: Set[Tuple[str, str, str]] = set()

    for key, values in connections.items():
        arr = list(values)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] in connections[arr[j]]:
                    triplets.add(tuple(sorted([key, arr[i], arr[j]])))

    if DEBUG:
        pprint(triplets)

    final_result = 0
    for n1, n2, n3 in triplets:
        if n1.startswith('t') or n2.startswith('t') or n3.startswith('t'):
            final_result += 1

    print(f'Part 1: {final_result}')

if __name__ == '__main__':
    run()