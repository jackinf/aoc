from dataclasses import dataclass

from day19.models.minerals import Minerals


@dataclass
class Wallet:
    minerals: Minerals

    def clone(self):
        return Wallet(minerals=self.minerals.copy())

    def total_in_ores(self, exchange):
        return self.minerals.ore \
            + self.minerals.clay * exchange['clay'] \
            + self.minerals.obsidian * exchange['obsidian'] \
            + self.minerals.geode * exchange['geode']
