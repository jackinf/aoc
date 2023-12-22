import re
from typing import List, Dict

with open('input.txt', 'r') as f:
    sections = f.read().split('\n\n')

workflows_raw = sections[0].split('\n')
ratings = sections[1].split('\n')
ratings = [[val.split('=') for val in rating[1:-1].split(',')] for rating in ratings]
ratings = [{val[0]: int(val[1]) for val in rating} for rating in ratings]


workflows = {}
for workflow_raw in workflows_raw:
    parts = workflow_raw[:-1].split('{')
    expression = re.split('[:,]', parts[1])
    workflows[parts[0]] = expression


def evaluate_expression(expression: List[str], rating: Dict[str, int]):
    index = 0

    while index < len(expression):
        if not ('>' in expression[index] or '<' in expression[index]):
            return expression[index]

        rating_key: str = expression[index][0]
        comparison_sign: str = expression[index][1]
        expr_val = int(expression[index][2:])
        rating_val = rating[rating_key]

        if comparison_sign == '>' and rating_val > expr_val or comparison_sign == '<' and rating_val < expr_val:
            index += 1
        else:
            index += 2

    raise Exception('should not get here')


total = 0
for rating in ratings:
    workflow_key = 'in'
    path = ['in']
    while True:
        expression = workflows[workflow_key]
        workflow_key = evaluate_expression(expression, rating)
        path.append(workflow_key)

        if workflow_key == 'R':
            path_str = '-> '.join(path)
            print(f'Rejected: {path_str}')
            break

        if workflow_key == 'A':
            curr_total = sum(rating.values())
            total += curr_total
            path_str = '-> '.join(path)
            print(f'Accepted: {path_str}, total: {curr_total}')
            break


print(f'Part 1: {total}')
