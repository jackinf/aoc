from dataclasses import dataclass

from day19.models.robot_cost_in_ores import RobotCostInOres


@dataclass
class SimplifiedBlueprint:
    id: int
    ore_robot_cost: RobotCostInOres
    geode_robot_cost: RobotCostInOres
