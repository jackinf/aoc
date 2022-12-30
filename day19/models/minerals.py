from dataclasses import dataclass


@dataclass(frozen=True)
class Minerals:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __add__(self, other: "Minerals") -> "Minerals":
        return Minerals(
            self.ore + other.ore,
            self.clay + other.clay,
            self.obsidian + other.obsidian,
            self.geode + other.geode
        )

    def __sub__(self, other) -> "Minerals":
        return Minerals(
            self.ore - other.ore,
            self.clay - other.clay,
            self.obsidian - other.obsidian,
            self.geode - other.geode
        )

    def __ge__(self, other: "Minerals") -> bool:
        return self.ore >= other.ore \
            and self.clay >= other.clay \
            and self.obsidian >= other.obsidian \
            and self.geode >= other.geode

    def negate(self):
        self.ore *= -1
        self.clay *= -1
        self.obsidian *= -1
        self.geode *= -1

    def copy(self) -> "Minerals":
        return Minerals(self.ore, self.clay, self.obsidian, self.geode)

    def get_by_type(self, type: str):
        match type:
            case "ore": return self.ore
            case "clay": return self.clay
            case "obsidian": return self.obsidian
            case "geode": return self.geode
