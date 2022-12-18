def find_intersections(cubes):
    intersections = set()

    for cube in cubes:
        x, y, z = cube
        nei1, nei2, nei3, nei4, nei5, nei6 = (x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)

        if nei1 in cubes:
            intersection = tuple(sorted((nei1, cube)))
            intersections.add(intersection)

        if nei2 in cubes:
            intersection = tuple(sorted((nei2, cube)))
            intersections.add(intersection)

        if nei3 in cubes:
            intersection = tuple(sorted((nei3, cube)))
            intersections.add(intersection)

        if nei4 in cubes:
            intersection = tuple(sorted((nei4, cube)))
            intersections.add(intersection)

        if nei5 in cubes:
            intersection = tuple(sorted((nei5, cube)))
            intersections.add(intersection)

        if nei6 in cubes:
            intersection = tuple(sorted((nei6, cube)))
            intersections.add(intersection)

    return intersections

def find_min_max(cubes):
    min_x, min_y, min_z = float('inf'), float('inf'), float('inf')
    max_x, max_y, max_z = float('-inf'), float('-inf'), float('-inf')

    for x, y, z in cubes:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)

        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)

    offset = 5
    return min_x - offset, min_y - offset, min_z - offset, max_x + offset, max_y + offset, max_z + offset


def bfs_airpockets(cubes, min_max):
    all_airpockets = set()
    min_x, min_y, min_z, max_x, max_y, max_z = min_max

    # start from physical cubes
    for cube in cubes:
        x, y, z = cube

        # get all the neighbors of the physical cube;
        for nei in [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]:
            # filter out physical neighbour cubes because we are interested only in airpockets
            if nei in cubes:
                continue
            # print('checking', nei)

            candidate_airpockets = set()  # let's start collecting candidates for airpockets
            seen = set()

            q = [nei]
            while q:
                curr = q.pop(0)
                x, y, z = curr

                if curr in cubes or curr in seen:
                    continue
                seen.add(curr)

                candidate_airpockets.add(curr)

                if x == min_x or x == max_x or y == min_y or y == max_y or z == min_z or z == max_z:
                    # We've reached the edge of the map, so this is not an airpocket
                    candidate_airpockets.clear()
                    break

                # traverse neighbors
                for nei in [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]:
                    if nei in cubes or nei in seen:  # it's not needed: it just speeds up the process
                        continue

                    q.append(nei)

            all_airpockets.update(candidate_airpockets)

    return all_airpockets


def count_sides_that_airpockets_touch(cubes, airpockets):
    touch_count = 0
    for airpocket in airpockets:
        x, y, z = airpocket
        for nei in [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]:
            if nei in cubes:
                touch_count += 1
    return touch_count



if __name__ == '__main__':
    with open('input.txt') as f:
        cubes = [line.strip().split(',') for line in f]
        cubes = set(tuple([int(x) for x in elem]) for elem in cubes)

    """
    Thought process:
        - cubes don't intersect
        - find only intersections - on xy, xz, and yz
        - each intersection substracts -2 points
        - initial points is a number of cubes * 6
    """

    side_count = len(cubes) * 6

    intersections = find_intersections(cubes)
    part1_result = side_count - len(intersections) * 2

    print(f'Result 1: {part1_result}')  # 4474

    minmax = find_min_max(cubes)
    all_airpockets = bfs_airpockets(cubes, minmax)
    airpocket_touch_count = count_sides_that_airpockets_touch(cubes, all_airpockets)

    part2_result = part1_result - airpocket_touch_count

    print(f'Result 2: {part2_result}')  # 2518