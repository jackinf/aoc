from typing import Dict, Tuple

from day19.models.blueprint import Blueprint
from day19.models.inventory import Inventory
from day19.models.minerals import Minerals
from day19.models.wallet import Wallet


class CurrencyManager:
    @staticmethod
    def generate_currency_exchange(blueprint: Blueprint) -> Dict[str, int]:

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

        return robot_costs_in_ores

    @staticmethod
    def get_total_in_ores(exchange: Dict[str, int], minerals: Minerals) -> int:
        return minerals.ore \
            + minerals.clay * exchange["clay"] \
            + minerals.obsidian * exchange["obsidian"] \
            + minerals.geode * exchange["geode"]

    @staticmethod
    def get_score(exchange: Dict[str, int], wallet: Wallet, inventory: Inventory) -> Tuple[int, int]:
        ore_in_ores = exchange["ore"]
        clay_in_ores = exchange["clay"]
        obsidian_in_ores = exchange["obsidian"]
        geode_in_ores = exchange["geode"]

        total = ore_in_ores + clay_in_ores + obsidian_in_ores + geode_in_ores
        coef0 = ore_in_ores / total
        coef1 = clay_in_ores / total
        coef2 = obsidian_in_ores / total
        coef3 = geode_in_ores / total

        # relative importance coefficents for each mineral
        coef0 = 1
        coef1 = 1
        coef2 = 1
        coef3 = 1
        mp = 1

        current_rate_of_collecting_ores = inventory.ore_robots * coef0 \
            + inventory.clay_robots * coef1 \
            + inventory.obsidian_robots * coef2 \
            + inventory.geode_robots * coef3

        upper_rate_of_collecting_ores = (inventory.ore_robots + 1) * coef0 \
            + (inventory.clay_robots + 1) * coef1 \
            + (inventory.obsidian_robots + 1) * coef2 \
            + (inventory.geode_robots + 1) * coef3

        current_ores_possessing = wallet.total_in_ores(exchange)

        current_rate_of_collecting_ores = (current_rate_of_collecting_ores + current_ores_possessing) * mp
        upper_rate_of_collecting_ores = (upper_rate_of_collecting_ores + current_ores_possessing) * mp

        return current_rate_of_collecting_ores, upper_rate_of_collecting_ores

    @staticmethod
    def get_score3(wallet: Wallet, inventory: Inventory, minutes_left: int):
        # calculate theoretical production

        # current amount of geodes
        curr_geodes = wallet.minerals.geode

        # all that could be produced with current amount of geode bots
        possible_geodes = inventory.geode_robots * minutes_left

        # possible geodes that could be produced if a geode bot was made for every remaining minute

        return curr_geodes + possible_geodes
