from dataclasses import dataclass

from day19.models.minerals import Minerals


@dataclass
class Wallet:
    minerals: Minerals

    def clone(self):
        return Wallet(minerals=self.minerals.copy())

    def add_minerals(self, minerals: Minerals):
        self.minerals += minerals