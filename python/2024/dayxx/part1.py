def read_input(file_name: str):
    with open(file_name) as f:
        blocks = f.read().split('\n\n')

    coords = {}
    for lines in blocks[0].split('\n'):
        k, v = lines.split(':')
        coords[k] = int(v)

    conditions = []
    for lines in blocks[1].split('\n'):
        k1, cond, k2, arrow, k3 = lines.split()
        conditions.append((k1, cond, k2, k3))


    return coords, conditions

def solve(coords, conditions):
    while conditions:
        condition = conditions.pop(0)
        k1, cond, k2, k3 = condition
        if k1 not in coords or k2 not in coords:
            conditions.append(condition)
            continue

        v1, v2 = coords[k1], coords[k2]

        if cond == 'AND':
            coords[k3] = v1 & v2
        elif cond == 'OR':
            coords[k3] = v1 | v2
        elif cond == 'XOR':
            coords[k3] = v1 ^ v2

def collect_z(coords):
    res = ''

    for k in sorted(coords.keys(), reverse=True):
        if k.startswith('z'):
            res += str(coords[k])

    return res

def run():
    coords, conditions = read_input('input.txt')
    solve(coords, conditions)
    result = collect_z(coords)
    result_int = int(result, 2)

    print(coords)
    print(conditions)

    print(f'Part 1: {result_int}')

if __name__ == '__main__':
    run()