import re
from collections import defaultdict, Counter
from dataclasses import dataclass
from pprint import pprint
from typing import List, Dict


def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2
    if op == "/":
        return num1 // num2
    raise Exception("operation not permitted")

@dataclass
class Monkey:
    index: int
    items: List[int]
    operation_args: List[str]
    divisible_by: int
    monkey_target_if_true: int
    monkey_target_if_false: int

    def inspect_items(self):
        new_recipients = []
        while self.items:
            item = self.items.pop(0)
            p1, op, p2 = self.operation_args
            p1 = item if p1 == "old" else int(p1)
            p2 = item if p2 == "old" else int(p2)
            new_worry = calculate(p1, p2, op)
            new_worry //= 3  # after monkey inspects an item but before throwing to another monkey
            target = self.monkey_target_if_true if new_worry % self.divisible_by == 0 else self.monkey_target_if_false
            new_recipients.append([target, new_worry])
        return new_recipients

    def add_item(self, item):
        self.items.append(item)

class MonkeyManager:
    def __init__(self, monkeys: Dict[int, Monkey]):
        self.monkeys = monkeys
        self.counter = Counter()

    def cycle_monkeys(self):
        for i, monkey in self.monkeys.items():
            recipients = monkey.inspect_items()
            for target, new_worry in recipients:
                self.monkeys[target].add_item(new_worry)
            self.counter[i] += len(recipients)  # keep track how many items have been inspected

    def output_monkey_standings(self):
        for i, monkey in monkeys.items():
            items_str = ', '.join(map(str, monkey.items))
            print(f'Monkey {i}. Inspected items: {self.counter[i]}. Current items: {items_str}')

    def calculate_monkey_business(self):
        p1, p2 = self.counter.most_common(2)[:2]
        return p1[1] * p2[1]


def extract_info(lines, pointer):
    def extract_number(offset):
        return int(re.findall(r'\d+', lines[pointer + offset]).pop())

    index = extract_number(0)
    items = [int(x) for x in re.findall(r'\d+', lines[pointer + 1])]  # starting items
    operation_args_eq_index = lines[pointer + 2].index("= ")
    operation_args = lines[pointer + 2][operation_args_eq_index + 1:].split()
    divisible_by = extract_number(3)  # assuming divisible by
    monkey_target_if_true = extract_number(4)
    monkey_target_if_false = extract_number(5)

    return Monkey(index, items, operation_args, divisible_by, monkey_target_if_true, monkey_target_if_false)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.read().split('\n')]

    monkeys = defaultdict(Monkey)

    # Parse monkeys
    for i, line, in enumerate(lines):
        if line.startswith('Monkey '):
            monkey = extract_info(lines, i)
            monkeys[monkey.index] = monkey

    # Cycle monkeys
    manager = MonkeyManager(monkeys)
    for i in range(20):
        print(f"Cycle: {i+1}")
        manager.cycle_monkeys()
        manager.output_monkey_standings()
        print()

    pprint(manager.counter)
    print(f'Result 1: {manager.calculate_monkey_business()}')
