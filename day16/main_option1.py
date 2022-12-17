# import re
# from collections import defaultdict
# from pprint import pprint
# from typing import List, Dict, Set, Tuple
#
# Valve = str
# Rate = int
# Score = int
# Valves = Set[Valve]
# ValvePaths = Dict[Valve, Set[Valve]]
# ValveRates = Dict[Valve, int]
# START_MINUTE = 1
# MAX_MINUTES = 30
# START_POS = "AA"
# Step: Tuple[int, int, set, int]
#
#
# def parse(lines: List[str]):
#     paths: ValvePaths = defaultdict(set)
#     rates: ValveRates = {}
#
#     for line in lines:
#         print(line)
#         match = re.search("Valve (?P<main>\w+) has flow rate=(?P<rate>\d+); (tunnels lead to valves|tunnel leads to valve) (?P<valves>.+)", line)
#         main_valve = match.group("main")
#         rate: Rate = int(match.group("rate"))
#         valves: List[Valve] = [valve.strip() for valve in match.group("valves").split(",")]
#
#         for valve in valves:
#             paths[main_valve].add(valve)
#             paths[valve].add(main_valve)
#             rates[main_valve] = rate
#
#     return paths, rates
#
#
# def get_unique_valves(paths: ValvePaths) -> Valves:
#     return set(paths.keys())
#
#
# def calculate_score(valves: Valves, rates: ValveRates) -> Score:
#     return sum(rates[valve] for valve in valves)
#
#
# def bfs(paths: ValvePaths, rates: ValveRates):
#     valves: Valves = get_unique_valves(paths)
#
#     # dd1 = {i:v for i,v in enumerate(valves)}
#     # dd2 = {v:i for i,v in dd1.items()}
#
#     q: List[Step] = [(START_POS, START_MINUTE, set(), 0)]
#     best_score = 0
#     seen = {}
#     while q:
#         valve, minute, open_valves, total_score = q.pop(0)
#         print(valve, minute, open_valves, total_score)
#
#         key = tuple(list(open_valves) + [valve, minute])
#         if key in seen and seen[key] <= total_score:
#             continue
#         seen[key] = total_score
#
#         best_score = max(best_score, total_score)
#         if minute > MAX_MINUTES:
#             continue
#
#         # option: moving to another valve
#         new_score = total_score + calculate_score(open_valves, rates)
#         for next_valve in paths[valve]:
#             next_step = (next_valve, minute + 1, open_valves, new_score)
#             q.append(next_step)
#
#         # option: opening a valve
#         # curr_valve_open = open_valves & dd2[valve]
#         curr_valve_open = valve in open_valves
#         if not curr_valve_open:
#             # open_valves += 1 << dd2[valve]  # open valve
#             open_valves = set(open_valves)
#             open_valves.add(valve)
#
#             new_score = total_score + calculate_score(open_valves, rates)
#             next_step = (valve, minute + 1, open_valves, new_score)
#             q.append(next_step)
#
#     print(best_score)
#
#
# if __name__ == '__main__':
#     with open('sample.txt') as f:
#         lines = [line.strip() for line in f]
#     print(lines)
#
#     paths, rates = parse(lines)
#     # pprint(paths)
#     # pprint(rates)
#
#     bfs(paths, rates)