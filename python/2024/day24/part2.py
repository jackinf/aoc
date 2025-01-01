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
    cache, rules = read_file('sample3.txt')

    for key in rules:
        get_val(cache, rules, key)

    """
    I DO NOT UNDERSTAND THE REQUIREMENTS!
    
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1

y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

(x) 101010 + (y) 101100 = (z) 1010110

x00 AND y00 -> z05 0
x01 AND y01 -> z02 0
x02 AND y02 -> z01 0
x03 AND y03 -> z03 1
x04 AND y04 -> z04 0
x05 AND y05 -> z00 1


???

EXAMPLE 2:

x00: 1
x01: 1
x02: 0
x03: 1

y00: 1
y01: 0
y02: 1
y03: 1




    """

    # combined = ''
    # for key in sorted(cache, reverse=True):
    #     if key.startswith('z'):
    #         combined += str(cache[key])
    #
    # print(int(combined, 2))


if __name__ == '__main__':
    run()