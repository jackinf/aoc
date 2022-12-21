from dataclasses import dataclass

from day19.models.minerals import Minerals


@dataclass
class OreWallet:
    ores: int = 0
    geodes: int = 0

    def clone(self):
        return OreWallet(ores=self.ores)

    def add_ores(self, minerals: Minerals):
        self.ores += minerals.ore
        self.geodes += minerals.geode
