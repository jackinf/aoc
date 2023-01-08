from collections import Counter


cache = {}

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


def update_counts(counts, letter, sign=1):
    match letter:
        case 'N': counts[0] += (1 * sign)
        case 'B': counts[1] += (1 * sign)
        case 'C': counts[2] += (1 * sign)
        case 'H': counts[3] += (1 * sign)


def counts_to_str(counts):
    word = ''
    word += 'N' * counts[0]
    word += 'B' * counts[1]
    word += 'C' * counts[2]
    word += 'H' * counts[3]
    return Counter(word)


def solve(letter1, letter2, depth, rules):
    if depth == 0:
        counts_start = [0, 0, 0, 0]
        update_counts(counts_start, letter1)
        update_counts(counts_start, letter2)
        return counts_start

    key = (letter1, letter2, depth)
    if depth in cache:
        return cache[key]

    new_letter = rules[letter1 + letter2]

    counts1 = solve(letter1, new_letter, depth - 1, rules)
    counts2 = solve(new_letter, letter2, depth - 1, rules)

    # merge counts
    counts = [0, 0, 0, 0]
    for i in range(len(counts)):
        counts[i] += counts1[i]
        counts[i] += counts2[i]
    update_counts(counts, new_letter, -1)

    cache[key] = counts
    return counts


if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]

    template = list(lines.pop(0))
    lines.pop(0)

    rules = {}
    while lines:
        line = lines.pop(0)
        source, dest = line.split('->')
        source = source.strip()
        dest = dest.strip()
        rules[source] = dest

    counts = [0, 0, 0, 0]
    # for letter in template:
    #     update_counts(counts, letter)

    steps = 40
    for i in range(len(template) - 1):
        counts_ = solve(template[i], template[i+1], steps, rules)
        print(f'f({template[i]}{template[i+1]}, {steps}) = ', counts_to_str(counts_))

        for i in range(len(counts)):
            counts[i] += counts_[i]

    for i in range(1, len(template) - 1):
        update_counts(counts, template[i], -1)

    print(f"FINAL: f({''.join(template)}, {steps}) = ", counts_to_str(counts))
    # print('final', counts)
    print(f'Min: {min(counts)}, Max: {max(counts)}, Result: {max(counts) - min(counts)}')

    # print(f'Result 2: {res}')
