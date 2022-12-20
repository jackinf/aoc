from dataclasses import dataclass
from typing import List

# from day19.types import PhraseType


@dataclass
class RobotCost:
    ore: int
    clay: int
    obsidian: int
    geode: int

    @staticmethod
    def create_from(phrases: List[str]) -> "RobotCost":
        ore, clay, obsidian, geode = 0, 0, 0, 0

        for phrase in phrases:
            split = phrase.split(' ')
            count, name = int(split[0]), split[1]

            ore += count if name == "ore" else 0
            clay += count if name == "clay" else 0
            obsidian += count if name == "obsidian" else 0
            geode += count if name == "geode" else 0

        return RobotCost(ore, clay, obsidian, geode)


@dataclass
class Blueprint:
    ore_robot_cost: RobotCost
    clay_robot_cost: RobotCost
    obsidian_robot_cost: RobotCost
    geode_robot_cost: RobotCost