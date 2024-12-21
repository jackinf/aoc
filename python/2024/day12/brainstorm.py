from collections import defaultdict
import math

def organize_and_count_turns(walls_dict):
    def find_next_wall(current_wall, remaining_walls):
        x1, y1, x2, y2 = current_wall
        for wall in remaining_walls:
            wx1, wy1, wx2, wy2 = wall
            if (x2, y2) == (wx1, wy1):
                return wall, (wx2, wy2)
            if (x2, y2) == (wx2, wy2):
                return wall, (wx1, wy1)
            if (x1, y1) == (wx1, wy1):
                return wall, (wx2, wy2)
            if (x1, y1) == (wx2, wy2):
                return wall, (wx1, wy1)
        return None, None

    def count_turns(loop):
        def angle_between(p1, p2, p3):
            dx1, dy1 = p2[0] - p1[0], p2[1] - p1[1]
            dx2, dy2 = p3[0] - p2[0], p3[1] - p2[1]
            dot = dx1 * dx2 + dy1 * dy2
            det = dx1 * dy2 - dy1 * dx2
            return math.atan2(det, dot)

        turn_count = 0
        for i in range(len(loop)):
            p1 = loop[i - 1]
            p2 = loop[i]
            p3 = loop[(i + 1) % len(loop)]
            angle = angle_between(p1, p2, p3)
            if abs(angle) > 1e-6:
                turn_count += 1
        return turn_count

    result = {}
    for symbol, walls in walls_dict.items():
        walls = set(walls)
        loop = []

        # Start with a random wall
        current_wall = walls.pop()
        loop.append((current_wall[0], current_wall[1]))
        loop.append((current_wall[2], current_wall[3]))

        while walls:
            next_wall, next_point = find_next_wall(current_wall, walls)
            if not next_wall:
                break
            walls.remove(next_wall)
            loop.append(next_point)
            current_wall = next_wall

        # Remove duplicate endpoint
        if loop[0] == loop[-1]:
            loop.pop()

        # Count turns
        turns = count_turns(loop)
        result[symbol] = (loop, turns)

    return result

# Example input
walls_dict = defaultdict(set, {
    'A': {(6, 3, 6, 4), (0, 6, 1, 6), (3, 0, 4, 0), (4, 3, 5, 3), (1, 4, 1, 5),
          (3, 2, 3, 3), (0, 2, 0, 3), (3, 6, 4, 6), (1, 3, 2, 3), (1, 5, 2, 5),
          (5, 6, 6, 6), (2, 6, 3, 6), (6, 1, 6, 2), (5, 0, 6, 0), (6, 4, 6, 5),
          (0, 5, 0, 6), (4, 0, 5, 0), (1, 3, 1, 4), (3, 1, 4, 1), (1, 0, 2, 0),
          (0, 3, 0, 4), (2, 3, 3, 3), (2, 5, 3, 5), (3, 1, 3, 2), (0, 0, 0, 1),
          (0, 0, 1, 0), (6, 5, 6, 6), (4, 1, 5, 1), (5, 1, 5, 2), (2, 0, 3, 0),
          (3, 4, 3, 5), (0, 4, 0, 5), (6, 0, 6, 1), (6, 2, 6, 3), (5, 2, 5, 3),
          (3, 3, 4, 3), (4, 6, 5, 6), (1, 6, 2, 6), (3, 3, 3, 4), (0, 1, 0, 2)},
    'B': {(1, 4, 1, 5), (4, 1, 5, 1), (4, 3, 5, 3), (3, 2, 3, 3), (5, 1, 5, 2),
          (1, 3, 2, 3), (1, 5, 2, 5), (2, 5, 3, 5), (3, 4, 3, 5), (1, 3, 1, 4),
          (5, 2, 5, 3), (3, 1, 4, 1), (3, 3, 4, 3), (2, 3, 3, 3), (3, 3, 3, 4),
          (3, 1, 3, 2)}})

# Run the function
result = organize_and_count_turns(walls_dict)

# Print results
for symbol, (loop, turns) in result.items():
    print(f"Symbol: {symbol}")
    print(f"Loop: {loop}")
    print(f"Turns: {turns}\n")
