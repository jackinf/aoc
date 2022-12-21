from typing import Tuple

from day19.managers.shop import Shop
from day19.models.inventory import Inventory
from day19.models.ore_wallet import OreWallet
from day19.models.simplified_blueprint import SimplifiedBlueprint


class Simulation:
    # TODO: this program is currently too slow... optimize the game
    def simulate(self, blueprint: SimplifiedBlueprint):
        most_geodes_count = 0
        max_minute = 1
        max_minutes = 24

        shop = Shop(blueprint)

        starting_minute = 1
        starting_wallet = OreWallet(ores=0)
        starting_robots = Inventory(ore_robot=1, clay_robot=0, obsidian_robot=0, geode_robot=0)
        q = [(starting_wallet, starting_robots, starting_minute)]

        while q:
            step: Tuple[OreWallet, Inventory, int] = q.pop(0)
            wallet, inventory, minute = step

            max_minute = max(max_minute, minute)
            print(f'\rMax minute: {max_minute}, Max geodes: {most_geodes_count}, Queue size: {len(q)}', end="", flush=True)

            if minute > max_minutes:
                most_geodes_count = max(most_geodes_count, wallet.geodes)
                continue

            # Scenario 1: Try to buy a robot
            for robot_type in ["ore", "clay", "obsidian", "geode"]:
                if not shop.can_buy_robot(robot_type, wallet):
                    continue
                new_wallet, new_inventory = wallet.clone(), inventory.clone()

                collected_minerals = inventory.collect_minerals_using_robots()
                shop.buy_robot(robot_type, new_wallet, new_inventory)
                new_wallet.add_ores(collected_minerals)

                q.append([new_wallet, new_inventory, minute + 1])

            # Scenario 2: Just wait (not sure if I need to clone wallet & inventory)
            wallet.add_ores(inventory.collect_minerals_using_robots())
            q.append([wallet, inventory, minute + 1])

        print('most_geodes_count', most_geodes_count)
        return blueprint.id * most_geodes_count
