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

lowest_location = float('inf')
for seed in seeds:
    source, curr_value = 'seed', seed
    while source in paths:
        dest = paths[source]
        mapping_rules = mapping_rules_groups[get_mapping_rules_groups_key(source, dest)]
        for dest_range_start, source_range_start, length in mapping_rules:
            """
                    source_range [===================] source_range + length
                                        |
                                      curr
                    diff is       [=====]
                    dest_range            [#######]
                    dest_range + diff     [#######][=====]
            """
            if source_range_start <= curr_value < source_range_start + length:
                diff = curr_value - source_range_start
                curr_value = dest_range_start + diff
                break  # assuming there's only 1 mapping, thus break the for-loop
        source = dest
    assert source == 'location'
    lowest_location = min(lowest_location, curr_value)

print(f'Part 1: {lowest_location}')