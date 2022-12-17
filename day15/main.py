import re
from typing import List, Tuple, Set

Sensor = Tuple[int, int]
Beacon = Tuple[int, int]
SbPair = Tuple[Sensor, Beacon]
HalfWidth = int
SensorReach = Tuple[Sensor, HalfWidth]
MinMax = Tuple[Tuple[int, int], Tuple[int, int]]  # ((min-x, min-y), (max-x, max-y))
Coord = Tuple[int, int]
Interval = Tuple[Coord, Coord]

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

def get_yth_row_beacons_xs(y: int, sb_pairs: List[SbPair]) -> List[int]:
    coordinates = list(set(beacon for sensor, beacon in sb_pairs if beacon[1] == y))
    return [x for x, y in coordinates]

def get_yth_row_sensors_xs(y: int, sb_pairs: List[SbPair]) -> List[int]:
    coordinates = list(set(sensor for sensor, beacon in sb_pairs if sensor[1] == y))
    return [x for x, y in coordinates]

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
    intervals: List[Interval] = []

    for reach in reaches:
        sensor, hw = reach
        sx, sy = sensor

        start = sx - hw, y
        end = sx + hw, y
        intervals.append((start, end))

    return sorted(intervals)

def merge_yth_row_intervals(y: int, intervals: List[Interval]) -> List[Coord]:
    assert all(start[1] == end[1] == y for start, end in intervals)

    x_intervals = [[start[0], end[0]] for start, end in intervals]
    x_intervals.sort()

    new_x_intervals: List[List[int]] = []

    for i in range(len(intervals)):
        if i == 0:
            new_x_intervals.append(x_intervals[0])
            continue

        prev_start_x, prev_end_x = new_x_intervals[-1]
        curr_start_x, curr_end_x = x_intervals[i]

        # expand previous interval
        if curr_start_x <= prev_end_x <= curr_end_x:
            new_x_intervals[-1] = [prev_start_x, curr_end_x]
            continue

        # add new interval
        if curr_start_x > prev_end_x:
            new_x_intervals.append([curr_start_x, curr_end_x])
            continue

    return [(coord[0], coord[1]) for coord in new_x_intervals]

def count_occupied_cells(x_intervals: list[Coord], sensors_xs: List[int], beacon_xs: List[int]) -> int:
    total = sum(end - start + 1 for start, end in x_intervals)
    for start, end in x_intervals:
        for beacon_x in beacon_xs:
            if start <= beacon_x <= end:
                total -= 1
        for sensors_x in sensors_xs:
            if start <= sensors_x <= end:
                total -= 1
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        y = 2000000

    sb_pairs = parse(lines)

    # 1. calculate sensor half-heights (& half-widths) => call them "reach"
    reaches = calculate_reaches(sb_pairs)

    # 2. find sensors that reach the y-th row -> get xy-coord + "reach". Every time sensor moves down-up y-axis, reach is reduced by 1
    reaches = convert_sensors_to_yth_row(y, reaches)

    # 3. get minimum & maximum x on y-th row
    minmax = get_minmax(sb_pairs)

    # 4. convert to intervals
    intervals = convert_reaches_to_intervals(reaches)

    # 5. merge intervals
    x_intervals = merge_yth_row_intervals(y, intervals)

    # 6. check already existing sensors & beacons on y-th row
    yth_row_sensor_xs = get_yth_row_sensors_xs(y, sb_pairs)
    yth_row_beacon_xs = get_yth_row_beacons_xs(y, sb_pairs)

    # 7. count covered cells by intervals
    result1 = count_occupied_cells(x_intervals, yth_row_sensor_xs, yth_row_beacon_xs)
    print(f'Result 1: {result1}')


