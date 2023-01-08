from collections import Counter


cache = {}
rules = {}

"""
    f(NC, 2) => NBC => f(NB, 1) + f(BC, 1)

    f(NB, 1) => NBB => f(NB, 0) + f(BB, 0) - B
    
    f(NB, 0) => [1, 1, 0, 0]
    f(BB, 0) => [0, 2, 0, 0]
    ...
    f(NB, 1) => NBB => [1, 1, 0, 0] + [0, 2, 0, 0] - [0, 1, 0, 0] = [1, 2, 0, 0]
    cache[(NB, 1)] = [1, 2, 0, 0]
    
    ====
    
    f(NNCB, 0) => f(NN, 0) + f(NC, 0) + f(CB, 0) - N - C
    
"""


"""
    [N, B, C, H]
"""


def solve(letters, depth):
    if depth == 0:
        return Counter(letters)

    key = (depth, *letters)
    if key in cache:
        return cache[key]

    if len(letters) > 2:
        left, middle, right = letters[:-1], letters[-2], letters[-2:]
        counter = solve(left, depth) + solve(right, depth)
        counter[middle] -= 1
    elif len(letters) == 2:
        middle = rules[''.join(letters)]
        left, right = [letters[0], middle], [middle, letters[1]]
        counter = solve(left, depth - 1) + solve(right, depth - 1)
        counter[middle] -= 1
    else:
        raise Exception('should not happen')

    cache[(depth, *letters)] = counter
    return counter


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    template = list(lines.pop(0))
    lines.pop(0)

    while lines:
        line = lines.pop(0)
        source, dest = line.split('->')
        source = source.strip()
        dest = dest.strip()
        rules[source] = dest

    counts = [0, 0, 0, 0]

    steps = 40
    final_counter = solve(template, steps)

    mc = final_counter.most_common()
    res = mc[0][1] - mc[-1][1]
    print(f'Result 2: {res}')

