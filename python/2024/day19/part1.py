from functools import cache


DEBUG = False


def read_input():
    with open('input.txt') as f:
        blocks = f.read().split('\n\n')
        patterns = blocks[0].split(', ')
        designs = blocks[1].split('\n')

    return set(patterns), designs


def run():
    patterns, designs = read_input()

    @cache
    def check_match(design: str) -> bool:
        if design == '':
            return True

        for pattern in patterns:
            if design.startswith(pattern) and check_match(design[len(pattern):]):
                return True

        return False

    matches = 0
    for design_index, design_val in enumerate(designs):
        if DEBUG:
            print(f"Design '{design_val}': {design_index + 1} out of {len(designs)}")

        if check_match(design_val):
            matches += 1

    print(f'Part 1: {matches}')


run()