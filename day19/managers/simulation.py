from collections import defaultdict
from typing import Tuple

from day19.managers.log_manager import LogManager
from day19.managers.currency_manager import CurrencyManager
from day19.managers.shop import Shop
from day19.models.blueprint import Blueprint
from day19.models.inventory import Inventory
from day19.models.minerals import Minerals
from day19.models.wallet import Wallet


class Simulation:
    # TODO: this program is currently too slow... optimize the game
    def simulate(self, blueprint: Blueprint):
        most_geodes_count = 0
        max_minute = 1
        max_minutes = 24

        shop = Shop(blueprint)

        starting_minute = 1
        starting_wallet = Wallet(Minerals())
        starting_robots = Inventory(ore_robots=1, clay_robots=0, obsidian_robots=0, geode_robots=0)
        q = [(starting_wallet, starting_robots, starting_minute, '')]
        best_log = ''

        exchange = CurrencyManager.generate_currency_exchange(blueprint)
        best_scores = defaultdict(int)
        best_ores = defaultdict(int)

        while q:
            step: Tuple[Wallet, Inventory, int, str] = q.pop(0)
            wallet, inventory, minute, log = step

            most_geodes_count = max(most_geodes_count, wallet.minerals.geode)
            print(f'\rMax minute: {max(max_minute, minute)}, '
                  f'Max geodes: {most_geodes_count}, '
                  f'Queue size: {len(q)}',
                  end="", flush=True)

            if minute > max_minutes:
                if most_geodes_count <= wallet.minerals.geode:
                    most_geodes_count = wallet.minerals.geode
                    best_log = log
                continue

            log += f"\n\n== Minute {minute} =="

            # TODO: Define Heuristic
            score_curr = CurrencyManager.get_score3(wallet, inventory, max_minutes - minute)
            tot = wallet.total_in_ores(exchange)
            if best_scores[minute] > score_curr and best_ores[minute] > tot:
                continue
            best_scores[minute] = score_curr
            best_ores[minute] = tot

            # Try to buy a robot
            for robot_type in ["geode", "obsidian", "clay", "ore"]:
                if not shop.can_buy_robot(robot_type, wallet, inventory):
                    continue

                new_wallet, new_inventory = wallet.clone(), inventory.clone()

                # Spend first: takes money out of wallet, inventory not yet affected
                ordered_robot_type, ordered_qty, paid = shop.pay_for_robot(robot_type, new_wallet)
                log2 = LogManager.log_spent_to_build(log, ordered_robot_type, ordered_qty, paid)

                # Collect minerals
                collected_minerals = new_inventory.collect_minerals_using_robots()
                new_wallet.minerals += collected_minerals
                log2 = LogManager.log_how_many_collected(log2, new_inventory, collected_minerals, new_wallet)

                # Collect the created robot
                shop.receive_robot(ordered_robot_type, ordered_qty, new_inventory)
                log2 = LogManager.log_created_robot(log2, robot_type, new_inventory)

                q.append((new_wallet, new_inventory, minute + 1, log2))

            # Just wait & collect ores
            new_wallet, new_inventory = wallet.clone(), inventory.clone()
            collected_minerals = new_inventory.collect_minerals_using_robots()
            new_wallet.minerals += collected_minerals
            log2 = LogManager.log_how_many_collected(log, new_inventory, collected_minerals, new_wallet)

            q.append((new_wallet, new_inventory, minute + 1, log2))

        print('most_geodes_count', most_geodes_count)
        print('best_log')
        print(best_log)

        return blueprint.id * most_geodes_count
