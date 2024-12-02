import sys

with open('input.txt', 'r') as f:
    info_groups = f.read().split('\n\n')

seeds = [int(value) for value in info_groups.pop(0).split(':')[1].split()]
mapping_rules_groups = {}
paths = {}

get_mapping_rules_groups_key = lambda source_arg, dest_arg: f'{source_arg}-{dest_arg}'

# parse
for info in info_groups:
    name, value_lines_str = info.split(':')
    values = [[int(value) for value in value_line.split()] for value_line in value_lines_str.split('\n')]
    values.pop(0)  # as str is in format "\n50 98 2\n52 50 48" then the first value is "", thus pop it

    source, to, dest = name.split()[0].split('-')
    paths[source] = dest
    mapping_rules_groups[get_mapping_rules_groups_key(source, dest)] = values

paths_reversed = {dst: src for src, dst in paths.items()}

assert len(seeds) % 2 == 0

# takes 1-2 minutes to get an answer
counter = 0
while True:
    source = 'location'
    curr_value = counter
    while source in paths_reversed:
        dest = paths_reversed[source]
        mapping_rules = mapping_rules_groups[get_mapping_rules_groups_key(dest, source)]
        for source_range_start, dest_range_start, length in mapping_rules:
            if source_range_start <= curr_value < source_range_start + length:
                diff = curr_value - source_range_start
                curr_value = dest_range_start + diff
                break
        source = dest

        # final check
        if source == 'seed':
            for i in range(0, len(seeds), 2):
                if seeds[i] <= curr_value < seeds[i] + seeds[i+1]:
                    print(f'Part 2: {counter}, {curr_value}')
                    sys.exit()
    counter += 1
