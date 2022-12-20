from typing import Tuple

from day19.managers.shop import Shop
from day19.models.blueprint import Blueprint
from day19.models.inventory import Inventory
from day19.models.minerals import Minerals
from day19.models.wallet import Wallet


class Simulation:
    # TODO: this program is currently too slow... optimize the game
    def simulate(self, blueprint: Blueprint):
        most_geodes_count = 0
        max_minutes = 24

        shop = Shop(blueprint)

        starting_minute = 1
        starting_wallet = Wallet(Minerals(ore=0, clay=0, obsidian=0, geode=0))
        starting_robots = Inventory(ore_robot=1, clay_robot=0, obsidian_robot=0, geode_robot=0)
        q = [(starting_wallet, starting_robots, starting_minute)]

        while q:
            step: Tuple[Wallet, Inventory, int] = q.pop(0)
            wallet, inventory, minute = step

            if minute > max_minutes:
                most_geodes_count = max(most_geodes_count, wallet.minerals.geode)
                continue

            # Scenario 1: Try to buy a robot
            for robot_type in ["ore", "clay", "obsidian", "geode"]:
                if not shop.can_buy_robot(robot_type, wallet):
                    continue
                new_wallet, new_inventory = wallet.clone(), inventory.clone()

                collected_minerals = inventory.collect_minerals_using_robots()
                shop.buy_robot(robot_type, new_wallet, new_inventory)
                new_wallet.add_minerals(collected_minerals)

                q.append([new_wallet, new_inventory, minute + 1])

            # Scenario 2: Just wait (not sure if I need to clone wallet & inventory)
            wallet.add_minerals(inventory.collect_minerals_using_robots())
            q.append([wallet, inventory, minute + 1])

        print('most_geodes_count', most_geodes_count)
        return blueprint.id * most_geodes_count
