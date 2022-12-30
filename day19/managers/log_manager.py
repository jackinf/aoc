from day19.models.inventory import Inventory
from day19.models.minerals import Minerals
from day19.models.wallet import Wallet


class LogManager:
    @staticmethod
    def log_how_many_collected(log: str, inventory: Inventory, collected: Minerals, wallet: Wallet) -> str:
        if inventory.ore_robots > 0:
            log += f'\n{inventory.ore_robots} ore-collecting robots collects {collected.ore} ore; ' \
                   f'you now have {wallet.minerals.ore} ore.'

        if inventory.clay_robots > 0:
            log += f'\n{inventory.clay_robots} clay-collecting robots collects {collected.clay} clay; ' \
                   f'you now have {wallet.minerals.clay} clay.'

        if inventory.obsidian_robots > 0:
            log += f'\n{inventory.obsidian_robots} obsidian-collecting robots collects {collected.obsidian} obsidian; '\
                   f'you now have {wallet.minerals.obsidian} obsidian.'

        if inventory.geode_robots > 0:
            log += f'\n{inventory.geode_robots} geode-collecting robots collects {collected.geode} geode; ' \
                   f'you now have {wallet.minerals.geode} geode.'

        return log

    @staticmethod
    def log_created_robot(log: str, robot_type: str, inventory: Inventory) -> str:
        log += f"\nNew {robot_type}-collecting robot is ready; " \
               f"you now have {inventory.get_by_robot_type(robot_type)} of them"

        return log

    @staticmethod
    def log_spent_to_build(log: str, ordered_robot_type: str, ordered_qty: int, paid: Minerals) -> str:
        how_much_spent_arr = []
        if paid.ore > 0:
            how_much_spent_arr.append(f'{paid.ore} ore')

        if paid.clay > 0:
            how_much_spent_arr.append(f'{paid.clay} clay')

        if paid.obsidian > 0:
            how_much_spent_arr.append(f'{paid.obsidian} obsidian')

        if paid.geode > 0:
            how_much_spent_arr.append(f'{paid.geode} geode')

        if len(how_much_spent_arr) == 0:
            raise Exception("Why was nothing spent?")

        log += f"\nSpend {' and '.join(how_much_spent_arr)} to start building {ordered_qty} {ordered_robot_type}-collecting robots."

        return log
