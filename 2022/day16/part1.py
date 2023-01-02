from collections import defaultdict
from pprint import pprint
from typing import Set, Dict

from day16.parse_valves import parse_valves


def calculate_score(valves: Set[str], rates: Dict[str, int]) -> int:
    return sum(rates[valve] for valve in valves)


def traverse(paths, rates):
    # q = [('AA', 30, 0, set(), '')]
    q = []
    for nei in paths['AA']:
        q.append((nei, 29, 0, set(), ''))

    bests = defaultdict(lambda: -1)
    best_score = 0
    best_log = ''
    smallest_min_remaining = 30
    total_valves_to_open = len([node for node in paths.keys() if rates[node] > 0])

    while q:
        print(f'\r q={len(q)}, best_score={best_score}, smallest_min_remaining={smallest_min_remaining}', end='', flush=True)

        curr, minutes_remaining, flow_total, valves, log = q.pop(0)
        log += f'\n== Minute {30 - minutes_remaining + 1} ==\n'

        flow_rate = calculate_score(valves, rates)  # calculate score
        if valves:
            log += f"Valves {', '.join(valves)} are open, releasing {flow_rate} pressure.\n"
        else:
            log += "No valves are open.\n"

        # ending
        if minutes_remaining == 1:
            if best_score == flow_total:
                best_score = flow_total
                best_log = log
            continue

        # optimization
        if bests[curr] > flow_total:
            continue
        bests[curr] = flow_total

        flow_total += flow_rate
        best_score = max(best_score, flow_total)
        smallest_min_remaining = min(smallest_min_remaining, minutes_remaining)

        # we opened all the valves that can produce score; sit & wait
        if total_valves_to_open == len(valves):
            q.append((curr, minutes_remaining - 1, flow_total, valves.copy(), log))
            continue

        # go to a neighbour
        for nei in paths[curr]:
            q.append((nei, minutes_remaining - 1, flow_total, valves.copy(), log + f"You move to valve {nei}.\n"))

        # try to open a valve that has score >0
        if rates[curr] > 0 and curr not in valves:
            flow_total += rates[curr]
            valves.add(curr)

            q.append((curr, minutes_remaining - 1, flow_total, valves.copy(), log + f'You open valve {curr}.\n'))

    print()
    print('best_log')
    print(best_log)
    return best_score


if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]
    print(lines)

    paths, rates = parse_valves(lines)
    pprint(paths)
    print(rates)

    best_score = traverse(paths, rates)
    print(f'Result 1: {best_score}')  # 2320
