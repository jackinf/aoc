from collections import defaultdict


def count_closed_sides_in_grid(groups):
    closed_sides_count = 0
    intersections = set()

    for grouping_index, squares_set in groups.items():
        for a, b in squares_set:
            nei1, nei2, nei3, nei4 = (a-1, b), (a+1, b), (a, b-1), (a, b+1)

            if nei1 in squares_set:
                closed_sides_count += 1
                intersections.add((nei1, (a, b)))

            if nei2 in squares_set:
                closed_sides_count += 1
                intersections.add(((a, b), nei2))

            if nei3 in squares_set:
                closed_sides_count += 1
                intersections.add((nei3, (a, b)))

            if nei4 in squares_set:
                closed_sides_count += 1
                intersections.add(((a, b), nei4))

    return closed_sides_count, intersections

if __name__ == '__main__':
    with open('input.txt') as f:
        cubes = [line.strip().split(',') for line in f]
        cubes = [tuple([int(x) for x in elem]) for elem in cubes]

    # print(cubes)

    """
    Thought process:
        - cubes don't intersect
        - find only intersections - on xy, xz, and yz
        - each intersection substracts -2 points
        - initial points is a number of cubes * 6
    """

    side_count = len(cubes) * 6

    x_groups = defaultdict(set)
    y_groups = defaultdict(set)
    z_groups = defaultdict(set)

    for cube in cubes:
        x_groups[cube[0]].add((cube[1], cube[2]))
        y_groups[cube[1]].add((cube[0], cube[2]))
        z_groups[cube[2]].add((cube[1], cube[2]))

    xcount, int1 = count_closed_sides_in_grid(x_groups)
    ycount, int2 = count_closed_sides_in_grid(y_groups)
    zcount, int3 = count_closed_sides_in_grid(z_groups)

    all_int = int1.union(int2).union(int3)

    part1_result = side_count - len(all_int) * 2

    print(f'Result1: {part1_result}')