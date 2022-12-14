from typing import List, Tuple, Union

IntervalsCollection = List[List[Tuple[int, int]]]
PointsCollection = List[List[Tuple[int, int]]]
MinMax = Tuple[int, int, int, int]
WidthHeight = Tuple[int, int]
Grid = List[List[str]]


def parse_lines(lines: List[str]) -> IntervalsCollection:
    intervals = []
    for line in lines:
        intervals.append([])
        items = line.split('->')
        for item in items:
            pair = item.split(',')
            x, y = int(pair[0].strip()), int(pair[1].strip())
            intervals[-1].append((y, x))
    return intervals

def find_min_max(collections: IntervalsCollection):
    flattened = [x for y in collections for x in y]
    xs = [item[0] for item in flattened]
    ys = [item[1] for item in flattened]

    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    offset = 2  # for safety to avoid index out of bounds

    return minx - offset, maxx + offset, miny - offset, maxy + offset


def get_width_height(minmax: MinMax) -> WidthHeight:
    minx, maxx, miny, maxy = minmax
    height, width = maxy - miny + 1, maxx - minx + 1
    return width, height


def convert_to_0_based(minmax: MinMax, collections: Union[IntervalsCollection, PointsCollection]):
    new_collections = []
    minx, maxx, miny, maxy = minmax

    for collection in collections:
        new_collections.append([])
        for i in range(len(collection)):
            currx, curry = collection[i][0], collection[i][1]
            new_collections[-1].append((currx - minx, curry - miny))

    return new_collections


def convert_interval_to_points(intervals_collection: IntervalsCollection):
    points_collection: PointsCollection = []

    for intervals in intervals_collection:
        points_collection.append([])
        for i in range(1, len(intervals)):
            currx, curry = intervals[i][0], intervals[i][1]
            prevx, prevy = intervals[i-1][0], intervals[i-1][1]

            if currx - prevx == 0:
                step = 1 if curry > prevy else -1
                for y in range(prevy, curry + step, step):
                    points_collection[-1].append((currx, y))

            if curry - prevy == 0:
                step = 1 if currx > prevx else -1
                for x in range(prevx, currx + step, step):
                    points_collection[-1].append((x, curry))

    return points_collection

def create_grid(wh: WidthHeight, points_collections: PointsCollection) -> Grid:
    width, height = wh
    grid = [['.' for _ in range(height)] for _ in range(width)]

    for points in points_collections:
        for x, y in points:
            grid[x][y] = "#"

    return grid

def draw_grid(grid: Grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end='')
        print()
    print()


def pour_sand(sand_start: Tuple[int, int], grid: Grid):
    while True:
        row, col = sand_start
        row += 1
        while True:
            if is_oob((row + 1, col), grid):
                draw_grid(grid)
                return
            grid[row][col] = "~"

            if grid[row + 1][col] in [".", "~"]:
                row += 1
            elif grid[row + 1][col - 1] in [".", "~"]:
                row += 1
                col -= 1
            elif grid[row + 1][col + 1] in [".", "~"]:
                row += 1
                col += 1
            else:
                grid[row][col] = "o"
                break


def is_oob(coord: Tuple[int, int], grid: Grid) -> bool:
    return not (0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]))


def count_sand(grid: Grid):
    return len([x for y in grid for x in y if x == "o"])


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    sand_coord = (0, 500)
    sand_coord_wrapped = [[sand_coord]]

    intervals_collection = parse_lines(lines)
    minmax = find_min_max(intervals_collection + sand_coord_wrapped)
    wh = get_width_height(minmax)
    points_collection = convert_interval_to_points(intervals_collection)
    points_collection = convert_to_0_based(minmax, points_collection)
    sandx, sandy = convert_to_0_based(minmax, sand_coord_wrapped)[0][0]

    grid = create_grid(wh, points_collection)
    grid[sandx][sandy] = "+"

    pour_sand((sandx, sandy), grid)
    print(f'Result 1: {count_sand(grid)}')