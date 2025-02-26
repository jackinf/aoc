from re import findall
from typing import Iterable

PART_2_INCREASE = 10_000_000_000_000

# https://old.reddit.com/r/adventofcode/comments/1hd4wda/2024_day_13_solutions/
# https://advent-of-code.xavd.id/writeups/2024/day/13/

def find_intersection(
    a_x: int, a_y: int, b_x: int, b_y: int, x_prize: int, y_prize: int
) -> tuple[float, float]:
    """
    this solves:
    - a_x * a + b_x * b = x_prize
    - a_y * a + b_y * b = y_prize
    """

    # multiply out b_y and b_x (the coefficients of B)
    a_x_with_b_y = a_x * b_y
    x_prize_with_b_y = x_prize * b_y

    a_y_with_b_x = a_y * b_x
    y_prize_with_b_x = y_prize * b_x

    a = (x_prize_with_b_y - y_prize_with_b_x) / (a_x_with_b_y - a_y_with_b_x)

    b = (y_prize - a_y * a) / b_y

    return a, b


def parse_ints(l: Iterable[str]) -> list[int]:
    return [int(i) for i in l]


class Solution():
    _year = 2024
    _day = 13
    separator = "\n\n"

    def _solve(self, increase_distance=False) -> int:
        total = 0
        for block in self.input:
            vals = parse_ints(findall(r"\d+", block))
            if increase_distance:
                vals[4] += PART_2_INCREASE
                vals[5] += PART_2_INCREASE

            a, b = find_intersection(*vals)
            if a.is_integer() and b.is_integer():
                total += a * 3 + b

        return int(total)

    def part_1(self) -> int:
        return self._solve()

    def part_2(self) -> int:
        return self._solve(increase_distance=True)