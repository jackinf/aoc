from typing import Tuple

from day19.models.blueprint import Blueprint
from day19.models.inventory import Inventory
from day19.models.minerals import Minerals
from day19.models.wallet import Wallet


OrderType = Tuple[str, int, Minerals]

class Shop:
    def __init__(self, blueprint: Blueprint):
        self.blueprint = blueprint

    """
    Checks if available to buy
    """

    def can_buy_robot(self, robot_type: str, wallet: Wallet, inventory: Inventory):
        match robot_type:
            case "ore": return self.can_buy_ore_robot(wallet, inventory)
            case "clay": return self.can_buy_clay_robot(wallet, inventory)
            case "obsidian": return self.can_buy_obsidian_robot(wallet, inventory)
            case "geode": return self.can_buy_geode_robot(wallet)
            case _: return False

    def can_buy_ore_robot(self, wallet: Wallet, inventory: Inventory):
        if inventory.ore_robots + wallet.minerals.ore >= self.blueprint.max_ores_needed():
            return False
        return wallet.minerals >= self.blueprint.ore_robot_cost.minerals

    def can_buy_clay_robot(self, wallet: Wallet, inventory: Inventory):
        if inventory.clay_robots + wallet.minerals.clay >= self.blueprint.max_clays_needed():
            return False
        return wallet.minerals >= self.blueprint.clay_robot_cost.minerals

    def can_buy_obsidian_robot(self, wallet: Wallet, inventory: Inventory):
        if inventory.obsidian_robots + wallet.minerals.obsidian >= self.blueprint.max_obsidians_needed():
            return False
        return wallet.minerals >= self.blueprint.obsidian_robot_cost.minerals

    def can_buy_geode_robot(self, wallet: Wallet):
        return wallet.minerals >= self.blueprint.geode_robot_cost.minerals

    """
    Actions to buy
    """

    def pay_for_robot(self, robot_type: str, wallet: Wallet) -> OrderType:
        match robot_type:
            case "ore": return self.pay_for_ore_robot(wallet)
            case "clay": return self.pay_for_clay_robot(wallet)
            case "obsidian": return self.pay_for_obsidian_robot(wallet)
            case "geode": return self.pay_for_geode_robot(wallet)
            case _: raise Exception("unsupported robot type")

    def pay_for_ore_robot(self, wallet: Wallet) -> OrderType:
        to_pay = self.blueprint.ore_robot_cost.minerals
        wallet.minerals -= to_pay
        return "ore", 1, to_pay

    def pay_for_clay_robot(self, wallet: Wallet) -> OrderType:
        to_pay = self.blueprint.clay_robot_cost.minerals
        wallet.minerals -= to_pay
        return "clay", 1, to_pay

    def pay_for_obsidian_robot(self, wallet: Wallet) -> OrderType:
        to_pay = self.blueprint.obsidian_robot_cost.minerals
        wallet.minerals -= to_pay
        return "obsidian", 1, to_pay

    def pay_for_geode_robot(self, wallet: Wallet) -> OrderType:
        to_pay = self.blueprint.geode_robot_cost.minerals
        wallet.minerals -= to_pay
        return "geode", 1, to_pay

    def receive_robot(self, robot_type: str, qty: int, inventory: Inventory):
        match robot_type:
            case "ore": inventory.ore_robots += qty
            case "clay": inventory.clay_robots += qty
            case "obsidian": inventory.obsidian_robots += qty
            case "geode": inventory.geode_robots += qty
            case _: raise Exception("Unsupported robot type")
