from pprint import pprint

from day19.managers.parser_manager import ParserManager


if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]

    blueprints = ParserManager.parse(lines)
    pprint(blueprints)