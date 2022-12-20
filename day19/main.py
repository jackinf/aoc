import re
from pprint import pprint
from typing import List

from day19.models import Blueprint, RobotCost


class Parser:
    @staticmethod
    def parse(lines: List[str]) -> List[Blueprint]:
        blueprints = []

        for line in lines:
            match = re.search("Blueprint (?P<blueprint>\d+): "
                  "Each ore robot costs (?P<oreRobotCost>.+). "
                  "Each clay robot costs (?P<clayRobotCost>.+). "
                  "Each obsidian robot costs (?P<obsidianRobotCost>.+). "
                  "Each geode robot costs (?P<geodeRobotCost>.+).", line)

            ore_robot_cost_phrases: List[str] = [phrase.strip() for phrase in match.group("oreRobotCost").split('and')]
            clay_robot_cost_phrases: List[str] = [phrase.strip() for phrase in match.group("clayRobotCost").split('and')]
            obsidian_robot_cost_phrases: List[str] = [phrase.strip() for phrase in match.group("obsidianRobotCost").split('and')]
            geode_robot_cost_phrases: List[str] = [phrase.strip() for phrase in match.group("geodeRobotCost").split('and')]

            ore_robot_cost = RobotCost.create_from(ore_robot_cost_phrases)
            clay_robot_cost = RobotCost.create_from(clay_robot_cost_phrases)
            obsidian_robot_cost = RobotCost.create_from(obsidian_robot_cost_phrases)
            geode_robot_cost = RobotCost.create_from(geode_robot_cost_phrases)

            blueprints.append(Blueprint(
                ore_robot_cost=ore_robot_cost,
                clay_robot_cost=clay_robot_cost,
                obsidian_robot_cost=obsidian_robot_cost,
                geode_robot_cost=geode_robot_cost,
            ))

        return blueprints


if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]

    blueprints = Parser.parse(lines)
    pprint(blueprints)