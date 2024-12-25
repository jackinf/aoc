from collections import defaultdict
from typing import Tuple, List, Set, Dict

DEBUG = True


def read_input(file_name: str) -> List[Tuple[str, str]]:
    with open(file_name) as f:
        lines = f.read().split('\n')
        return [(line.split('-')[0], line.split('-')[1]) for line in lines]

def bron_kerbosch(acc_result: Set[str], potential: Set[str], excluded: Set[str], graph: Dict[str, Set[str]], cliques: List[Set[str]]):
    if not potential and not excluded:
        cliques.append(acc_result)
        return

    for v in list(potential):
        bron_kerbosch(
            acc_result.union({v}),
            potential.intersection(graph[v]),
            excluded.intersection(graph[v]),
            graph,
            cliques
        )
        potential.remove(v)
        excluded.add(v)


def run():
    pairs = read_input('input.txt')

    graph = defaultdict(set)
    for left, right in pairs:
        graph[left].add(right)
        graph[right].add(left)

    if DEBUG:
        print(graph)

    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    largest_clique = max(cliques, key=len)

    password = ','.join(sorted(largest_clique))
    print(f"Part 2: {password}")


if __name__ == '__main__':
    run()