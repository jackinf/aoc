from dataclasses import dataclass

from day19.models.minerals import Minerals


@dataclass
class Inventory:
    ore_robots: int
    clay_robots: int
    obsidian_robots: int
    geode_robots: int

    def collect_minerals_using_robots(self):
        # Each robot collects 1 mineral
        ore = self.ore_robots
        clay = self.clay_robots
        obsidian = self.obsidian_robots
        geode = self.geode_robots

        return Minerals(ore, clay, obsidian, geode)

    def clone(self):
        return Inventory(self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots)

    def get_by_robot_type(self, robot_type: str):
        match robot_type:
            case "ore": return self.ore_robots
            case "clay": return self.clay_robots
            case "obsidian": return self.obsidian_robots
            case "geode": return self.geode_robots
            case _: raise Exception("no such robot type")