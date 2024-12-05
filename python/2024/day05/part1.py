from collections import defaultdict
from typing import List, Dict, Set

with open('input.txt') as f:
    rules_raw, sections_raw = f.read().split('\n\n')


def analyze_section(row: List[int], rules_p: Dict[int, Set[int]]) -> int:
    for i in range(len(row) - 1):
        for j in range(i, len(row)):
            if row[i] in rules_p[row[j]]:
                return 0

    return row[len(row) // 2]


rules: Dict[int, Set[int]] = defaultdict(set)
for rule_raw in rules_raw.split('\n'):
    before, after = list(map(int, rule_raw.split('|')))
    rules[before].add(after)

final_result = 0
for i, section_raw in enumerate(sections_raw.split('\n')):
    section = list(map(int, section_raw.split(',')))
    result = analyze_section(section, rules)
    final_result += result

print(f'Part 1: {final_result}')