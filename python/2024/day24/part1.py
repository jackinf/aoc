def read_file(file_name: str):
    with open(file_name) as f:
        blocks = f.read().split('\n\n')

        cache = {}
        for line in blocks[0].split('\n'):
            left, right = line.split(': ')
            cache[left] = int(right)

        rules = {}
        for line in blocks[1].split('\n'):
            left, key = line.split(' -> ')
            left, op, right = left.split()
            rules[key] = (left, op, right)

        return cache, rules

def get_val(cache, rules, key) -> int:
    if key not in cache:
        left_key, op, right_key = rules[key]
        left_val = get_val(cache, rules, left_key)
        right_val = get_val(cache, rules, right_key)

        match op:
            case "AND": cache[key] = left_val & right_val
            case "OR": cache[key] = left_val | right_val
            case "XOR": cache[key] = left_val ^ right_val

    return cache[key]


def run():
    cache, rules = read_file('input.txt')

    for key in rules:
        get_val(cache, rules, key)

    combined = ''
    for key in sorted(cache, reverse=True):
        if key.startswith('z'):
            combined += str(cache[key])

    print(int(combined, 2))


if __name__ == '__main__':
    run()