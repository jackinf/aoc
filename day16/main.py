import re
from collections import defaultdict
from dataclasses import dataclass
from pprint import pprint
from typing import List, Dict, Set, Tuple

Valve = str
Rate = int
Score = int
Valves = Set[Valve]
ValvePaths = Dict[Valve, Set[Valve]]
ValveRates = Dict[Valve, int]
START_MINUTE = 1
MAX_MINUTES = 30
START_POS = "AA"
Step: Tuple[int, int, set, int]


def parse(lines: List[str]) -> Tuple[ValvePaths, ValveRates]:
    paths: ValvePaths = defaultdict(set)
    rates: ValveRates = {}

    for line in lines:
        match = re.search("Valve (?P<main>\w+) has flow rate=(?P<rate>\d+); (tunnels lead to valves|tunnel leads to valve) (?P<valves>.+)", line)
        main_valve = match.group("main")
        rate: Rate = int(match.group("rate"))
        valves: List[Valve] = [valve.strip() for valve in match.group("valves").split(",")]

        for valve in valves:
            paths[main_valve].add(valve)
            paths[valve].add(main_valve)
            rates[main_valve] = rate

    return paths, rates


def get_unique_valves(paths: ValvePaths) -> Valves:
    return set(paths.keys())


def calculate_score(valves: Valves, rates: ValveRates) -> Score:
    return sum(rates[valve] for valve in valves)

def make_full_map_key(p1: str, p2: str):
    return '-'.join(sorted([p1, p2]))


def construct_full_map(paths, rates):
    full_map = defaultdict(set)

    for key in sorted(paths.keys()):
        seen = set()
        q = [(key, 0)]
        while q:
            cand, depth = q.pop(0)

            if cand in seen:
                continue
            seen.add(cand)
            if rates[key] > 0 and rates[cand] > 0 and key != cand:
                full_map[key].add((cand, depth))

            for new_cand in paths[cand]:
                q.append((new_cand, depth + 1))

    # return full_map
    return {k:v for k,v in full_map.items()}


@dataclass
class Step:
    prev_pos: str
    curr_pos: str
    curr_score: int
    prev_minute: int
    curr_minute: int
    curr_open_valves: set
    log: str


def traverse(full_map: Dict[str, Set[Tuple[str, int]]], paths, rates):
    q: List[Step] = []
    for start_pos in paths['AA']:
        if rates[start_pos] == 0:
            continue

        step = Step(
            prev_pos='AA',
            curr_pos=start_pos,
            curr_score=0,
            prev_minute=0,
            curr_minute=1,
            curr_open_valves=set(),
            log=''
        )
        q.append(step)

    best_score = 0
    best_log = ''
    all_valves_len = len(full_map)

    # We always open a valve when we arrive at position. The movement is not done in 1 step, rather in multiple steps
    while q:
        # extract step values
        step = q.pop(0)
        prev_pos = step.prev_pos
        curr_pos = step.curr_pos
        curr_score = step.curr_score
        prev_minute = step.prev_minute
        curr_minute = step.curr_minute
        curr_open_valves = step.curr_open_valves
        log = step.log

        # if made it to the last minute - finish the item
        if curr_minute > 30:
            best_score, best_log = max(best_score, curr_score), log
            continue

        # calculate current score based on opened valves
        minutes_spent_moving = curr_minute - prev_minute
        released_pressure_per_minute = calculate_score(curr_open_valves, rates)
        total_released_pressure = released_pressure_per_minute * minutes_spent_moving
        curr_score += total_released_pressure
        log += f' |=== MINUTE {curr_minute}: {prev_pos} -> {curr_pos} (made {minutes_spent_moving} steps), {step.curr_score} + {released_pressure_per_minute} x {minutes_spent_moving} = {curr_score}p\n'

        if curr_pos not in curr_open_valves:
            released_pressure_per_minute = calculate_score(curr_open_valves, rates)
            curr_score += released_pressure_per_minute

            curr_open_valves.add(curr_pos)  # open the valve that we arrived to just now
            curr_minute += 1  # we spend 1 minute opening the valve
            log += f' |=== MINUTE {curr_minute}: opened {curr_pos} valve, {step.curr_score} + {released_pressure_per_minute} x {minutes_spent_moving} = {curr_score}p\n'
            # log += f' |=== #{curr_minute}: opened {curr_pos} valve. All opened valves: {", ".join(curr_open_valves)}\n'

        # update log
        # print(curr_pos, curr_score, curr_minute, curr_open_valves, log)

        # STAY: if as all valves are open, let's just wait another minute (or calculate the finishing time)
        if all_valves_len == len(curr_open_valves):
            step = Step(
                prev_pos=curr_pos,
                curr_pos=curr_pos,
                curr_score=curr_score,
                prev_minute=curr_minute,
                curr_minute=curr_minute + 1,
                curr_open_valves=set(curr_open_valves),
                log=log
            )
            q.append(step)
            continue

        if curr_pos not in full_map:
            continue

        # MOVE: continue traversing other non-opened valves
        for new_cand, minutes_delta in full_map[curr_pos]:
            if new_cand in curr_open_valves:
                continue  # this one is open, skip

            step = Step(
                prev_pos=curr_pos,
                curr_pos=new_cand,
                curr_score=curr_score,
                prev_minute=curr_minute,
                curr_minute=curr_minute + minutes_delta,
                curr_open_valves=set(curr_open_valves),
                log=log
            )
            q.append(step)

    print(best_log)
    return best_score


if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]
    # print(lines)

    paths, rates = parse(lines)
    # pprint(paths)
    # pprint(rates)

    full_map = construct_full_map(paths, rates)
    # pprint(full_map)

    best_score = traverse(full_map, paths, rates)
    print(f'Result 1: {best_score}')