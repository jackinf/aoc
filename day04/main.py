from pprint import pprint
from typing import Tuple


def fully_intersect(section1: Tuple[int, int], section2: Tuple[int, int]) -> bool:
    section1_in_section2 = section1[0] <= section2[0] <= section2[1] <= section1[1]
    section2_in_section1 = section2[0] <= section1[0] <= section1[1] <= section2[1]

    return section1_in_section2 or section2_in_section1


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        lines = [x.split(',') for x in lines]
        lines = [[(int(y.split('-')[0]), int(y.split('-')[1])) for y in x] for x in lines]

    pprint(lines)

    full_intersections = sum(1 for sections in lines if fully_intersect(sections[0], sections[1]))

    print(f"Result 1: {full_intersections}")


