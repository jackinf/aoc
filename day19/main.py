from day19.managers.parser_manager import ParserManager
from day19.managers.simulation import Simulation

if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]

    blueprints = ParserManager.parse(lines)

    total_quality = 0
    for blueprint in blueprints:
        simulation = Simulation()
        quality = simulation.simulate(blueprint)
        print(f'Blueprint {blueprint.id} quality is: {quality}')

        total_quality += quality

    print(f'Result 1: {total_quality}')