from dataclasses import dataclass


@dataclass(frozen=True)
class Minerals:
    ore: int
    clay: int
    obsidian: int
    geode: int

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

    def copy(self) -> "Minerals":
        return Minerals(self.ore, self.clay, self.obsidian, self.geode)