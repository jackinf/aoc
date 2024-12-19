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
    def count_matches(design: str) -> int:
        # exact match: design equals to one of the patterns
        if design == '':
            return 1

        matches = 0
        for pattern in sorted(patterns):
            if design.startswith(pattern):
                matches += count_matches(design[len(pattern):])

        return matches


    all_matches = 0
    for design_index, design_val in enumerate(designs):
        matches = count_matches(design_val)
        all_matches += matches

        if DEBUG:
            print(f"Design '{design_val}': {design_index + 1} out of {len(designs)}")
            print(f'Found matches: {matches}')
            print()

    print(f'Part 2: {all_matches}')


run()