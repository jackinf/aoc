with open('input.txt') as f:
    content = f.read()

import re

groups = re.findall('(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', content)

final_result = 0
enabled = True
for group in groups:
    operation, values_str = group[:-1].split('(')

    if operation == "don't":
        enabled = False
    elif operation == "do":
        enabled = True
    elif operation == "mul" and enabled:
        val1, val2 = list(map(int, values_str.split(',')))
        final_result += val1 * val2

print(f'Part 2: {final_result}')