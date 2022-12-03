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


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().split('\n')

    compartments = [divide_items_into_compartments(line) for line in lines if line.strip()]
    uniques_items = [get_unique_item(*compartment) for compartment in compartments]
    priorities = generate_priorities()
    unique_items_priorities = [priorities[unique] for unique in uniques_items]

    print(f"Result 1: {sum(unique_items_priorities)}")