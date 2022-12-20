from dataclasses import dataclass

from day19.models.minerals import Minerals


@dataclass
class Inventory:
    ore_robot: int
    clay_robot: int
    obsidian_robot: int
    geode_robot: int

    def collect_minerals_using_robots(self):
        # Each robot collects 1 mineral
        ore = self.ore_robot
        clay = self.clay_robot
        obsidian = self.obsidian_robot
        geode = self.geode_robot

        return Minerals(ore, clay, obsidian, geode)

    def clone(self):
        return Inventory(self.ore_robot, self.clay_robot, self.obsidian_robot, self.geode_robot)