import re
from typing import List, Tuple

Sensor = Tuple[int, int]
Beacon = Tuple[int, int]
SbPair = Tuple[Sensor, Beacon]
HalfWidth = int
SensorReach = Tuple[Sensor, HalfWidth]
MinMax = Tuple[Tuple[int, int], Tuple[int, int]]  # ((min-x, min-y), (max-x, max-y))

def parse(lines: List[str]) -> List[SbPair]:
    results = []

    for line in lines:
        match = re.search('Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)', line)
        sensor: Sensor = (int(match.group("sx")), int(match.group("sy")))
        beacon: Beacon = (int(match.group("bx")), int(match.group("by")))
        results.append((sensor, beacon))

    return results

def calculate_reaches(sb_pairs: List[SbPair]) -> List[SensorReach]:
    reaches: List[SensorReach] = []

    for sensor, beacon in sb_pairs:
        sx, sy = sensor
        bx, by = beacon

        reach: HalfWidth = abs(sx - bx) + abs(sy - by)

        reaches.append((sensor, reach))

    return reaches

def convert_sensors_to_yth_row(y: int, reaches: List[SensorReach]):
    new_reaches: List[SensorReach] = []

    for reach in reaches:
        sensor, half_width = reach
        sx, sy = sensor

        y_delta = y - sy

        # check if we can reach the y-th row
        if abs(y_delta) > half_width:
            continue

        new_sensor = (sx, sy + y_delta)
        new_half_width: HalfWidth = half_width - abs(y_delta)

        new_reaches.append((new_sensor, new_half_width))

    return new_reaches

def get_minmax(sb_pairs: List[SbPair]) -> MinMax:
    xs = [a[0] for b in sb_pairs for a in b]
    ys = [a[1] for b in sb_pairs for a in b]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    return (min_x, max_x), (min_y, max_y)

def convert_reaches_to_intervals(reaches: List[SensorReach]):
    pass  # TODO:

def merge_intervals(intervals):
    pass  # TODO

def count_occupied_cells(intervals):
    pass  # TODO

if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]
        y = 10

    sb_pairs = parse(lines)
    print(sb_pairs)

    # 1. calculate sensor half-heights (& half-widths) => call them "reach"
    reaches = calculate_reaches(sb_pairs)
    print(reaches)

    # 2. find sensors that reach the y-th row -> get xy-coord + "reach". Every time sensor moves down-up y-axis, reach is reduced by 1
    reaches = convert_sensors_to_yth_row(y, reaches)
    print(reaches)

    # 3. get minimum & maximum x on y-th row
    minmax = get_minmax(sb_pairs)
    print(minmax)


