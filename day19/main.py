from pprint import pprint

from day19.managers.parser_manager import ParserManager
from day19.managers.robot_cost_converter import RobotCostConverter
from day19.managers.simulation import Simulation

if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]

    blueprints = ParserManager.parse(lines)

    simplified_blueprints = []
    for blueprint in blueprints:
        simplified_blueprints.append(RobotCostConverter().simplify_blueprint(blueprint))
    pprint(simplified_blueprints)

    total_quality = 0
    for blueprint in simplified_blueprints[:1]:
        simulation = Simulation()
        quality = simulation.simulate(blueprint)
        print(f'Blueprint {blueprint.id} quality is: {quality}')

        total_quality += quality

    print(f'Result 1: {total_quality}')