from collections import Counter

if __name__ == '__main__':
    with open('input.txt') as f:
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

    step = 1
    while step <= 10:
        insertions = []

        for rule in rules:
            for i in range(len(template) - 1):
                if template[i] == rule[0] and template[i + 1] == rule[1]:
                    insertions.append((rules[rule], i + 1))

        for letter, at in sorted(insertions, key= lambda insertion: -insertion[1]):
            template.insert(at, letter)

        # print(step, ''.join(template))

        step += 1

    counter = Counter(template)
    mc = counter.most_common()
    print(mc)
    res = mc[0][1] - mc[-1][1]
    print(f'Result 1: {res}')
