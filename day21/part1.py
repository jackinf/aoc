if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    dd = {}
    res = {}

    for line in lines:
        if len(line) == 17:
            items = line.split(' ')
            target, source1, op, source2 = items
            dd[target[:4]] = (source1, source2, op)
        else:
            items = line.split(' ')
            target, numstr = items
            res[target[:4]] = int(numstr)

    def dfs(curr):
        if curr in res:
            return res[curr]
        s1, s2, op = dd[curr]
        r1 = dfs(s1)
        r2 = dfs(s2)
        match op:
            case "+": res[curr] = r1 + r2
            case "-": res[curr] = r1 - r2
            case "*": res[curr] = r1 * r2
            case "/": res[curr] = r1 // r2
            case _: raise Exception("no")
        return res[curr]

    part1 = dfs("root")

    print(f'Result 1: {part1}')  # 379578518396784

