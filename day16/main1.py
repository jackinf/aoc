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
            rates[main_valve] = rate

    return paths, rates


if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]
    print(lines)

    paths, rates = parse(lines)
    print(paths)
    print(rates)

    # TODO: implement alternative solution
