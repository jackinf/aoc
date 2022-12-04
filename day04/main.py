from typing import Tuple


def fully_intersect(section1: Tuple[int, int], section2: Tuple[int, int]) -> bool:
    section1_in_section2 = section1[0] <= section2[0] <= section2[1] <= section1[1]
    section2_in_section1 = section2[0] <= section1[0] <= section1[1] <= section2[1]

    return section1_in_section2 or section2_in_section1


def partially_intersect(section1: Tuple[int, int], section2: Tuple[int, int]) -> bool:
    return section1[0] <= section2[0] <= section1[1] or section2[0] <= section1[0] <= section2[1]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        lines = [x.split(',') for x in lines]
        lines = [[(int(y.split('-')[0]), int(y.split('-')[1])) for y in x] for x in lines]

    full_intersections = sum(1 for sections in lines if fully_intersect(*sections))

    print(f"Result 1: {full_intersections}")

    partial_intersections = sum(1 for sections in lines if partially_intersect(*sections))

    print(f"Result 2: {partial_intersections}")
