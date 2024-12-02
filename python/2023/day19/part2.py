import re
from pprint import pprint
from typing import List, Dict

# Fail
with open('input.txt', 'r') as f:
    sections = f.read().split('\n\n')

workflows_raw = sections[0].split('\n')
workflows = {}
for workflow_raw in workflows_raw:
    parts = workflow_raw[:-1].split('{')
    expression = re.split('[:,]', parts[1])
    workflows[parts[0]] = expression


def evaluate_expression(expression: List[str], total):
    index = 0

    # I have no idea what i'm doing here
    curr_total = total
    totals = [1 for _ in range(len(expression))]
    totals[0] = total

    combinations = []
    while index < len(expression):
        if not ('>' in expression[index] or '<' in expression[index]):
            return combinations

        comparison_sign: str = expression[index][1]
        expr_val = int(expression[index][2:])

        left_key = expression[index + 1]
        right_key = expression[index + 2]

        if comparison_sign == '>':
            left_total = curr_total * (4000 - expr_val + 1)
            right_total = curr_total * (expr_val - 1)
            combinations.append((left_key, left_total))
            combinations.append((right_key, right_total))
        elif comparison_sign == '<':
            left_total = curr_total * (expr_val - 1)
            right_total = curr_total * (4000 - expr_val + 1)
            combinations.append((left_key, left_total))
            combinations.append((right_key, right_total))

        index += 2

    raise Exception('should not get here')


q = [('in', 1)]
while q:
    workflow_key, total = q.pop(0)
    expression = workflows[workflow_key]
    workflow_key, total = evaluate_expression(expression, total)

    if workflow_key == 'R':
        break

    if workflow_key == 'A':
        print(f'total: {total}')
        break


# pprint(workflows)

# print(f'Part 2: {total}')
