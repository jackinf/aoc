from day19b.parse_blueprints import parse_blueprints
from day19b.run_blueprint_bfs import run_blueprint_bfs
from day19b.run_blueprint_dfs import run_blueprint_dfs


if __name__ == '__main__':
    """
    This is a quick & dirty solution, focused on the speed of the implementation of solution 
    """

    with open('sample.txt') as f:
        lines = [line.strip() for line in f]

    blueprints = parse_blueprints(lines)

    part1 = 0
    for id, blueprint in enumerate(blueprints):
        # we don't need more because some robots don't require more minerals,
        # otherwise we will be collecting minerals faster than we could produce robots
        maxspend = [
            max([row[0] for row in blueprint]),
            max([row[1] for row in blueprint]),
            max([row[2] for row in blueprint]),
            float('inf')  # we want more geodes as possible
        ]

        # BFS is very slow, and not 100% sure it works...
        # res = run_blueprint_bfs(blueprint, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])

        res = run_blueprint_dfs(blueprint, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
        print(f'id: {id + 1}, res: {res}')
        part1 += (id + 1) * res

    print(f'Result 1: {part1}')  # 1650
