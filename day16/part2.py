from collections import defaultdict
from pprint import pprint
from typing import Set, Dict

from day16.parse_valves import parse_valves


def calculate_score(valves: Set[str], rates: Dict[str, int]) -> int:
    return sum(rates[valve] for valve in valves)


# TODO: this solution is wrong
def traverse(paths, rates):
    q = [(0, 'AA', 'AA', 26, 0, set(), '')]
    # q = []
    # for nei in paths['AA']:
    #     q.append((nei, 29, 0, set(), ''))

    curr_bests = defaultdict(lambda: -1)
    best_score = 0
    best_log = ''
    smallest_min_remaining = 26
    total_valves_to_open = len([node for node in paths.keys() if rates[node] > 0])

    while q:
        print(f'\r q={len(q)}, best_score={best_score}, smallest_min_remaining={smallest_min_remaining}', end='', flush=True)

        # heap_score, curr, eleph, minutes_remaining, flow_total, valves, log = heapq.heappop(q)
        heap_score, curr, eleph, minutes_remaining, flow_total, valves, log = q.pop(0)

        log += f'\n== Minute {26 - minutes_remaining + 1} ==\n'

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

        # TODO: think of an optimization

        flow_total += flow_rate
        best_score = max(best_score, flow_total)
        smallest_min_remaining = min(smallest_min_remaining, minutes_remaining)

        # we opened all the valves that can produce score; sit & wait
        if total_valves_to_open == len(valves):
            q.append((flow_total, curr, eleph, minutes_remaining - 1, flow_total, valves.copy(), log))
            continue

        # go to a neighbour
        for curr_nei in paths[curr]:
            log2 = str(log)
            log2 += f"You move to valve {curr_nei}.\n"

            # ...and elephant either goes to a neighbour as well...
            for eleph_nei in paths[eleph]:
                log2 += f"Elephant moves to valve {eleph_nei}.\n"

                item = (flow_total, curr_nei, eleph_nei, minutes_remaining - 1, flow_total, valves.copy(), log2)
                q.append(item)
                # heapq.heappush(q, item)

            # ...or opens the valve (if valve is not open or value is > 0)
            if rates[eleph] > 0 and eleph not in valves:
                flow_total += rates[eleph]
                valves.add(eleph)
                log2 += f'Elephant opens valve {eleph}.\n'

                item = (flow_total, curr_nei, eleph, minutes_remaining - 1, flow_total, valves.copy(), log2)
                q.append(item)
                # heapq.heappush(q, item)

        # try to open (if valve is not open or value is > 0)
        if rates[curr] > 0 and curr not in valves:
            log2 = str(log)
            log2 += f"You open valve {curr}.\n"

            flow_total += rates[curr]
            valves.add(curr)

            # ...and elephant either goes to a neighbour...
            for eleph_nei in paths[eleph]:
                log2 += f"Elephant moves to valve {eleph_nei}.\n"

                item = (flow_total, curr, eleph_nei, minutes_remaining - 1, flow_total, valves.copy(), log2)
                q.append(item)
                # heapq.heappush(q, item)

            # ...or opens the valve (if valve is not open or value is > 0)
            if rates[eleph] > 0 and eleph not in valves:
                flow_total += rates[eleph]
                valves.add(eleph)
                log2 += f'Elephant opens valve {eleph}.\n'

                item = (flow_total, curr, eleph, minutes_remaining - 1, flow_total, valves.copy(), log2)
                q.append(item)
                # heapq.heappush(q, item)

    print()
    print('best_log')
    print(best_log)
    return best_score


def find_part2(paths, rates):
    best = 0
    for i in range(1):
        best = max(best, traverse(paths, rates))
    return best


if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]
    print(lines)

    paths, rates = parse_valves(lines)
    pprint(paths)
    print(rates)

    best_score = traverse(paths, rates)
    print(f'Result 2: {best_score}')
