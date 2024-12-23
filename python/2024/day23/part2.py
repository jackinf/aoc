from collections import defaultdict
from typing import Tuple, List, Set

DEBUG = False


def read_input(file_name: str) -> List[Tuple[str, str]]:
    with open(file_name) as f:
        lines = f.read().split('\n')
        return [(line.split('-')[0], line.split('-')[1]) for line in lines]


def run():
    pairs = read_input('input.txt')

    graph = defaultdict(set)
    for left, right in pairs:
        graph[left].add(right)
        graph[right].add(left)

    if DEBUG:
        print(graph)

    def dfs(node: str, seen: Set[str]):
        if node in seen:
            return
        seen.add(node)

        for nei in graph[node]:
            dfs(nei, seen)

    best = 0
    final_res = ''
    for key in graph:
        seen = set()

        dfs(key, seen)
        res = len(seen)

        if res > best:
            best = res
            final_res = ','.join(sorted(list(seen)))
            if DEBUG:
                print(key, res)

    print(f'Part 2: {final_res}')

if __name__ == '__main__':
    run()