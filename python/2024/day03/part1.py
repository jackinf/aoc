with open('input.txt') as f:
    content = f.read()

import re

groups = re.findall('mul\(\d+,\d+\)', content)
final_result = 0
for group in groups:
    operation, values_str = group[:-1].split('(')
    val1, val2 = list(map(int, values_str.split(',')))

    result = val1 * val2
    final_result += result

print(f'Part 1: {final_result}')
