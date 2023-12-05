from pprint import pprint

with open('sample.txt', 'r') as f:
    info_groups = f.read().split('\n\n')
    print(info_groups)

seeds = [int(value) for value in info_groups.pop(0).split(':')[1].split()]
mapping_rules_groups = {}
paths = {}

print(seeds)

get_mapping_rules_groups_key = lambda source_arg, dest_arg: f'{source_arg}-{dest_arg}'

# parse
for info in info_groups:
    name, value_lines_str = info.split(':')
    values = [[int(value) for value in value_line.split()] for value_line in value_lines_str.split('\n')]
    values.pop(0)  # as str is in format "\n50 98 2\n52 50 48" then the first value is "", thus pop it

    source, to, dest = name.split()[0].split('-')
    paths[source] = dest
    mapping_rules_groups[get_mapping_rules_groups_key(source, dest)] = values

pprint(mapping_rules_groups)
pprint(paths)

lowest_location = float('inf')
assert len(seeds) % 2 == 0
for i in range(0, len(seeds), 2):
    seed_start, seed_length = seeds[i], seeds[i+1]
    for seed in range(seed_start, seed_start + seed_length):
        source, curr_value = 'seed', seed
        while source in paths:
            dest = paths[source]
            mapping_rules = mapping_rules_groups[get_mapping_rules_groups_key(source, dest)]
            for dest_range_start, source_range_start, length in mapping_rules:
                if source_range_start <= curr_value <= source_range_start + length:
                    diff = curr_value - source_range_start
                    curr_value = dest_range_start + diff
                    break  # assuming there's only 1 mapping, thus break the for-loop
            source = dest
        assert source == 'location'
        lowest_location = min(lowest_location, curr_value)

print(f'Part 2: {lowest_location}')