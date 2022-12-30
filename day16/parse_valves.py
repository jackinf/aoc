import re
from collections import defaultdict
from typing import List, Dict, Set, Tuple

Valve = str
Rate = int
Valves = Set[Valve]
ValvePaths = Dict[Valve, Set[Valve]]
ValveRates = Dict[Valve, int]


def parse_valves(lines: List[str]) -> Tuple[ValvePaths, ValveRates]:
    paths: Dict[str, Set[str]] = defaultdict(set)
    rates: Dict[str, int] = {}

    for line in lines:
        match = re.search("Valve (?P<main>\w+) has flow rate=(?P<rate>\d+); (tunnels lead to valves|tunnel leads to valve) (?P<valves>.+)", line)
        main_valve = match.group("main")
        rate: Rate = int(match.group("rate"))
        valves: List[Valve] = [valve.strip() for valve in match.group("valves").split(",")]

        for valve in valves:
            paths[main_valve].add(valve)
            rates[main_valve] = rate

    return paths, rates



