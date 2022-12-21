from day19.models.inventory import Inventory
from day19.models.ore_wallet import OreWallet
from day19.models.simplified_blueprint import SimplifiedBlueprint


class Shop:
    def __init__(self, blueprint: SimplifiedBlueprint):
        self.blueprint = blueprint

    """
    Checks if available to buy
    """

    def can_buy_robot(self, robot_type: str, wallet: OreWallet):
        match robot_type:
            case "ore": return self.can_buy_ore_robot(wallet)
            case "clay": return self.can_buy_clay_robot(wallet)
            case "obsidian": return self.can_buy_obsidian_robot(wallet)
            case "geode": return self.can_buy_geode_robot(wallet)

    def can_buy_ore_robot(self, wallet: OreWallet):
        return wallet.ores >= self.blueprint.ore_robot_cost.ores

    def can_buy_clay_robot(self, wallet: OreWallet):
        return False

    def can_buy_obsidian_robot(self, wallet: OreWallet):
        return False

    def can_buy_geode_robot(self, wallet: OreWallet):
        return wallet.ores >= self.blueprint.geode_robot_cost.ores

    """
    Actions to buy
    """

    def buy_robot(self, robot_type: str, wallet: OreWallet, inventory: Inventory):
        match robot_type:
            case "ore": return self.buy_ore_robot(wallet, inventory)
            case "clay": return self.buy_clay_robot(wallet, inventory)
            case "obsidian": return self.buy_obsidian_robot(wallet, inventory)
            case "geode": return self.buy_geode_robot(wallet, inventory)

    def buy_ore_robot(self, wallet: OreWallet, inventory: Inventory) -> OreWallet:
        inventory.ore_robot += 1
        return OreWallet(ores=wallet.ores - self.blueprint.ore_robot_cost.ores)

    def buy_clay_robot(self, wallet: OreWallet,inventory: Inventory):
        raise Exception("cannot buy clay robot")

    def buy_obsidian_robot(self, wallet: OreWallet, inventory: Inventory):
        raise Exception("cannot buy obsidian robot")

    def buy_geode_robot(self, wallet: OreWallet, inventory: Inventory):
        inventory.geode_robot += 1
        return OreWallet(ores=wallet.ores - self.blueprint.geode_robot_cost.ores)