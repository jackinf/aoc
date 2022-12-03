from typing import List


def divide_items_into_compartments(items: str):
    return items[:len(items) // 2], items[len(items) // 2:]


def get_unique_item(first_compartment, second_compartment):
    return (set(first_compartment) & set(second_compartment)).pop()


def generate_priorities():
    priorities = {}
    for i in range(1, 27):
        priorities[chr(ord('a') + i - 1)] = i
    for i in range(27, 53):
        priorities[chr(ord('A') + i - 26 - 1)] = i
    return priorities


def get_unique_per_group_of_3_people(line1: str, line2: str, line3: str):
    return (set(line1) & set(line2) & set(line3)).pop()


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().split('\n')

    compartments = [divide_items_into_compartments(line) for line in lines if line.strip()]
    uniques_items = [get_unique_item(*compartment) for compartment in compartments]
    priorities = generate_priorities()
    unique_items_priorities = [priorities[unique] for unique in uniques_items]

    print(f"Result 1: {sum(unique_items_priorities)}")

    total_priority_for_groups_of_3_people = 0
    for i in range(0, len(lines), 3):
        unique_item = get_unique_per_group_of_3_people(lines[i], lines[i + 1], lines[i + 2])
        total_priority_for_groups_of_3_people += priorities[unique_item]

    print(f"Result 2: {total_priority_for_groups_of_3_people}")

