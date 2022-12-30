from dataclasses import dataclass

from day19.models.robot_cost import RobotCost


@dataclass
class Blueprint:
    id: int
    ore_robot_cost: RobotCost
    clay_robot_cost: RobotCost
    obsidian_robot_cost: RobotCost
    geode_robot_cost: RobotCost

    def get_robot_cost(self, robot_type: str) -> RobotCost:
        match robot_type:
            case "ore": return self.ore_robot_cost
            case "clay": return self.clay_robot_cost
            case "obsidian": return self.obsidian_robot_cost
            case "geode": return self.geode_robot_cost

    def max_ores_needed(self):
        return max(self.ore_robot_cost.minerals.ore, self.clay_robot_cost.minerals.ore, self.obsidian_robot_cost.minerals.ore, self.geode_robot_cost.minerals.ore)

    def max_clays_needed(self):
        return max(self.ore_robot_cost.minerals.clay, self.clay_robot_cost.minerals.clay, self.obsidian_robot_cost.minerals.clay, self.geode_robot_cost.minerals.clay)

    def max_obsidians_needed(self):
        return max(self.ore_robot_cost.minerals.obsidian, self.clay_robot_cost.minerals.obsidian, self.obsidian_robot_cost.minerals.obsidian, self.geode_robot_cost.minerals.obsidian)
