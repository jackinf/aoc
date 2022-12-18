from collections import defaultdict


def find_intersections(cubes):
    closed_sides_count = 0
    intersections = set()

    for cube in cubes:
        x, y, z = cube
        nei1, nei2, nei3, nei4, nei5, nei6 = (x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)

        if nei1 in cubes:
            closed_sides_count += 1
            intersection = tuple(sorted((nei1, cube)))
            intersections.add(intersection)

        if nei2 in cubes:
            closed_sides_count += 1
            intersection = tuple(sorted((nei2, cube)))
            intersections.add(intersection)

        if nei3 in cubes:
            closed_sides_count += 1
            intersection = tuple(sorted((nei3, cube)))
            intersections.add(intersection)

        if nei4 in cubes:
            closed_sides_count += 1
            intersection = tuple(sorted((nei4, cube)))
            intersections.add(intersection)

        if nei5 in cubes:
            closed_sides_count += 1
            intersection = tuple(sorted((nei5, cube)))
            intersections.add(intersection)

        if nei6 in cubes:
            closed_sides_count += 1
            intersection = tuple(sorted((nei6, cube)))
            intersections.add(intersection)

    return closed_sides_count, intersections

if __name__ == '__main__':
    with open('input.txt') as f:
        cubes = [line.strip().split(',') for line in f]
        cubes = set(tuple([int(x) for x in elem]) for elem in cubes)

    # print(cubes)

    """
    Thought process:
        - cubes don't intersect
        - find only intersections - on xy, xz, and yz
        - each intersection substracts -2 points
        - initial points is a number of cubes * 6
    """

    side_count = len(cubes) * 6

    closed_sides_count, intersections = find_intersections(cubes)

    part1_result = side_count - len(intersections) * 2

    print(f'Result1: {part1_result}')