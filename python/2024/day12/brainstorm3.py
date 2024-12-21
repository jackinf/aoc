from collections import defaultdict


def connect_walls(walls):
    # Separate horizontal and vertical walls
    horizontal_walls = []
    vertical_walls = []

    for wall in walls:
        x1, y1, x2, y2 = wall
        if y1 == y2:  # Horizontal
            horizontal_walls.append((x1, x2, y1))
        elif x1 == x2:  # Vertical
            vertical_walls.append((y1, y2, x1))

    # Sort each group to facilitate chaining
    horizontal_walls.sort()
    vertical_walls.sort()

    # Chain walls
    def chain_walls(walls, is_horizontal):
        chained = []
        while walls:
            start = walls.pop(0)
            chain = [start]
            while walls:
                next_wall = None
                for i, wall in enumerate(walls):
                    if is_horizontal:
                        if chain[-1][1] == wall[0] and chain[-1][2] == wall[2]:
                            next_wall = walls.pop(i)
                            break
                    else:
                        if chain[-1][1] == wall[0] and chain[-1][2] == wall[2]:
                            next_wall = walls.pop(i)
                            break
                if next_wall:
                    chain.append(next_wall)
                else:
                    break
            chained.append(chain)
        return chained

    horizontal_chains = chain_walls(horizontal_walls, is_horizontal=True)
    vertical_chains = chain_walls(vertical_walls, is_horizontal=False)

    return horizontal_chains, vertical_chains


# Convert back to original format
def chain_to_original(chain, is_horizontal):
    result = []
    for start, end, constant in chain:
        if is_horizontal:
            result.append((start, constant, end, constant))
        else:
            result.append((constant, start, constant, end))
    return result


# Input dictionary
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
          (3, 1, 3, 2)}
})

for key, walls in walls_dict.items():
    horizontal_chains, vertical_chains = connect_walls(walls)
    horizontal_chains = [chain_to_original(chain, is_horizontal=True) for chain in horizontal_chains]
    vertical_chains = [chain_to_original(chain, is_horizontal=False) for chain in vertical_chains]
    sides = len(horizontal_chains) + len(vertical_chains)
    print(f"Group {key}:")
    print(f"  Horizontal chains: {horizontal_chains}")
    print(f"  Vertical chains: {vertical_chains}")
    print(f"  Sides: {sides}")
