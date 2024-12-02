numbers_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def letters_to_numbers(line):
    accumulated_all = ''
    accumulated_numbers_only = ''

    for letter in line:
        accumulated_all += letter
        if letter.isnumeric():
            accumulated_numbers_only += letter
            continue

        for word, number in numbers_map.items():
            if len(accumulated_all) >= len(word) and accumulated_all[-len(word):] == word:
                accumulated_numbers_only += number

    return accumulated_numbers_only


with open('input.txt') as f:
    lines = [line for line in f.read().split('\n')]
    lines = [letters_to_numbers(line) for line in lines]

nums = [[x for x in line if x.isnumeric()] for line in lines]
sums = [int(x[0] + x[-1]) for x in nums]
total_sum = sum(sums)

print(f'Part 2: {total_sum}')