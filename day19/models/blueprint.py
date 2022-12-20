from dataclasses import dataclass

from day19.models.robot_cost import RobotCost


@dataclass
class Blueprint:
    id: int
    ore_robot_cost: RobotCost
    clay_robot_cost: RobotCost
    obsidian_robot_cost: RobotCost
    geode_robot_cost: RobotCost
