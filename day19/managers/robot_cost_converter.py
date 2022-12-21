from typing import Dict

from day19.models.blueprint import Blueprint
from day19.models.simplified_blueprint import SimplifiedBlueprint
from day19.models.robot_cost_in_ores import RobotCostInOres


class RobotCostConverter:
    def simplify_blueprint(self, blueprint: Blueprint) -> SimplifiedBlueprint:

        robot_costs_in_ores: Dict[str, int] = {}

        def get_core_cost(key):
            if key in robot_costs_in_ores:
                return robot_costs_in_ores[key]
            robot_costs_in_ores[key] = 0

            minerals = blueprint.get_robot_cost(key).minerals

            for other in ["ore", "clay", "obsidian", "geode"]:
                # you can't buy the robot for the same type that the same robot produces
                if other == key:
                    continue

                multiplier = minerals.get_by_type(other)
                if multiplier == 0:
                    continue

                robot_costs_in_ores[key] += get_core_cost(other) * multiplier

            return robot_costs_in_ores[key]

        robot_costs_in_ores["ore"] = 1  # that's a hack - just a currency, not an ore robot cost
        robot_costs_in_ores["geode"] = get_core_cost("geode")  # we are the most interested in this

        return SimplifiedBlueprint(
            id=blueprint.id,
            ore_robot_cost=RobotCostInOres(ores=blueprint.clay_robot_cost.minerals.ore),
            geode_robot_cost=RobotCostInOres(ores=robot_costs_in_ores["geode"]),
        )
