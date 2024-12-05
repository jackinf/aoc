from collections import defaultdict
from typing import List, Dict, Set

with open('input.txt') as f:
    rules_raw, sections_raw = f.read().split('\n\n')


def is_valid_section(row: List[int], rules_p: Dict[int, Set[int]]) -> bool:
    for i in range(len(row) - 1):
        for j in range(i, len(row)):
            if row[i] in rules_p[row[j]]:
                return False

    return True


def fix_section(row: List[int], rules_p: Dict[int, Set[int]]) -> int:
    for i in range(len(row) - 1):
        for j in range(i, len(row)):
            if row[i] in rules_p[row[j]]:
                row[i], row[j] = row[j], row[i]

    return row[len(row) // 2]


rules: Dict[int, Set[int]] = defaultdict(set)
for rule_raw in rules_raw.split('\n'):
    before, after = list(map(int, rule_raw.split('|')))
    rules[before].add(after)

broken_sections = []
for i, section_raw in enumerate(sections_raw.split('\n')):
    section = list(map(int, section_raw.split(',')))
    if not is_valid_section(section, rules):
        broken_sections.append(section)

final_result = 0
for broken_section in broken_sections:
    result = fix_section(broken_section, rules)
    final_result += result

print(f'Part 2: {final_result}')