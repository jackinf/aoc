from day19b.parse_blueprints import parse_blueprints
from day19b.run_blueprint_dfs import run_blueprint_dfs


if __name__ == '__main__':
    """
    This is a quick & dirty solution, focused on the speed of the implementation of solution 
    """

    with open('input.txt') as f:
        lines = [line.strip() for line in f][:3]

    blueprints = parse_blueprints(lines)

    part2 = 1
    for id, blueprint in enumerate(blueprints):
        # we don't need more because some robots don't require more minerals,
        # otherwise we will be collecting minerals faster than we could produce robots
        maxspend = [
            max([row[0] for row in blueprint]),
            max([row[1] for row in blueprint]),
            max([row[2] for row in blueprint]),
            float('inf')  # we want more geodes as possible
        ]

        res = run_blueprint_dfs(blueprint, maxspend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
        print(f'id: {id + 1}, res: {res}')
        part2 *= res

    print(f'Result 2: {part2}')  #
