import re
from typing import List


def parse_blueprints(lines: List[str]):
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