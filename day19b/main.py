import re
from pprint import pprint
from typing import List


def parse(lines: List[str]):
    blueprints = []
    for line in lines:
        items = re.split("[.:]", line)

        blueprint = [
            [0, 0, 0, 0],  # ore robot
            [0, 0, 0, 0],  # clay robot
            [0, 0, 0, 0],  # obs robot
            [0, 0, 0, 0],  # geode robot
        ]

        match1 = re.search("Each ore robot costs (?P<ore>\d+) ore", items[1])
        match2 = re.search("Each clay robot costs (?P<ore>\d+) ore", items[2])
        match3 = re.search("Each obsidian robot costs (?P<ore>\d+) ore and (?P<clay>\d+) clay", items[3])
        match4 = re.search("Each geode robot costs (?P<ore>\d+) ore and (?P<obs>\d+) obsidian", items[4])

        blueprint[0][0] = int(match1.group("ore"))
        blueprint[1][0] = int(match2.group("ore"))
        blueprint[2][0] = int(match3.group("ore"))
        blueprint[2][1] = int(match3.group("clay"))
        blueprint[3][0] = int(match4.group("ore"))
        blueprint[3][2] = int(match4.group("obs"))

        blueprints.append(blueprint)

    return blueprints


def run_blueprint(blueprint: List[List[int]]):
    end_minute = 24
    start_minute = 1
    start_robots = [1, 0, 0, 0]
    start_resources = [0, 0, 0, 0]
    max_geodes = 0
    max_minute = 1

    # find the quickest & best path till first geode

    q = [(start_minute, start_robots, start_resources)]
    while q:
        minute, robots, resources = q.pop(0)
        max_minute = max(max_minute, minute)
        print(f'\rq={len(q)}, geodes={max_geodes}, max_minute={max_minute}', end='', flush=True)

        if minute > end_minute:
            max_geodes = max(max_geodes, resources[3])

        # 0 - ore, 1 - clay, 2 - obs, 3 - geo
        for robot_type in [0, 1, 2, 3]:
            to_buy = blueprint[robot_type]

            res2 = resources[:]

            res2[0] -= to_buy[0]
            res2[1] -= to_buy[1]
            res2[2] -= to_buy[2]
            res2[3] -= to_buy[3]

            if res2[0] < 0 or res2[1] < 0 or res2[2] < 0 or res2[3] < 0:
                continue  # insufficient funds

            # collect
            res2[0] += robots[0]
            res2[1] += robots[1]
            res2[2] += robots[2]
            res2[3] += robots[3]

            # produce robot
            rob2 = robots[:]
            rob2[robot_type] += 1

            q.append((minute + 1, rob2, res2))

        # collect
        res2 = resources[:]
        res2[0] += robots[0]
        res2[1] += robots[1]
        res2[2] += robots[2]
        res2[3] += robots[3]

        q.append((minute + 1, robots[:], res2))

    print()
    return max_geodes


if __name__ == '__main__':
    """
    This is a quick & dirty solution, focused on the speed of the implementation of solution 
    """

    with open('sample.txt') as f:
        lines = [line.strip() for line in f]

    blueprints = parse(lines)

    part1 = 0
    for id, blueprint in enumerate(blueprints):
        part1 += (id + 1) * run_blueprint(blueprint)
    print(f'Result 1: {part1}')
