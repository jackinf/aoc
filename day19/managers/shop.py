from day19.models.blueprint import Blueprint
from day19.models.inventory import Inventory
from day19.models.wallet import Wallet


class Shop:
    def __init__(self, blueprint: Blueprint):
        self.blueprint = blueprint

    """
    Checks if available to buy
    """

    def can_buy_robot(self, robot_type: str, wallet: Wallet):
        match robot_type:
            case "ore": return self.can_buy_ore_robot(wallet)
            case "clay": return self.can_buy_clay_robot(wallet)
            case "obsidian": return self.can_buy_obsidian_robot(wallet)
            case "geode": return self.can_buy_geode_robot(wallet)

    def can_buy_ore_robot(self, wallet: Wallet):
        return wallet.minerals >= self.blueprint.ore_robot_cost.minerals

    def can_buy_clay_robot(self, wallet: Wallet):
        return wallet.minerals >= self.blueprint.clay_robot_cost.minerals

    def can_buy_obsidian_robot(self, wallet: Wallet):
        return wallet.minerals >= self.blueprint.obsidian_robot_cost.minerals

    def can_buy_geode_robot(self, wallet: Wallet):
        return wallet.minerals >= self.blueprint.geode_robot_cost.minerals

    """
    Actions to buy
    """

    def buy_robot(self, robot_type: str, wallet: Wallet, inventory: Inventory):
        match robot_type:
            case "ore": return self.buy_ore_robot(wallet, inventory)
            case "clay": return self.buy_clay_robot(wallet, inventory)
            case "obsidian": return self.buy_obsidian_robot(wallet, inventory)
            case "geode": return self.buy_geode_robot(wallet, inventory)

    def buy_ore_robot(self, wallet: Wallet, inventory: Inventory) -> Wallet:
        inventory.ore_robot += 1
        return Wallet(minerals=wallet.minerals - self.blueprint.ore_robot_cost.minerals)

    def buy_clay_robot(self, wallet: Wallet,inventory: Inventory):
        inventory.clay_robot += 1
        return Wallet(minerals=wallet.minerals - self.blueprint.clay_robot_cost.minerals)

    def buy_obsidian_robot(self, wallet: Wallet, inventory: Inventory):
        inventory.obsidian_robot += 1
        return Wallet(minerals=wallet.minerals - self.blueprint.obsidian_robot_cost.minerals)

    def buy_geode_robot(self, wallet: Wallet, inventory: Inventory):
        inventory.geode_robot += 1
        return Wallet(minerals=wallet.minerals - self.blueprint.geode_robot_cost.minerals)