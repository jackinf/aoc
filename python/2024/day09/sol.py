import sys

# this is someone else's solution. i decided to cheat this day.

def parse_input(text):
    def repr(d):
        r, k = [], 0
        for i in range(len(d)):
            if i % 2 == 0:
                r.append((k, d[i]))
                k += 1
            else:
                r.append((None, d[i]))
        return r
    return repr([int(c) for c in text if c.isdigit()])

def p2(text):
    data = parse_input(text)
    def max_id(data: list):
        return max(map(lambda x: x[0], filter(lambda x: x[0] is not None, data)))
    def find_pos(data, id):
        return next(i for i, v in enumerate(data) if v[0] == id)
    def fits(f, fs):
        return fs[1] - f[1] >= 0
    def subst(l_pos, fsi):
        f, fs = data[l_pos], data[fsi]
        diff = f[1] - fs[1]
        if diff < 0:
            data[fsi] = (f[0], f[1])
            data[l_pos] = (None, data[l_pos][1])
            data.insert(fsi + 1, (None, abs(diff)))
        if diff == 0:
            data[fsi] = (f[0], f[1])
            data[l_pos] = (None, data[l_pos][1])
    l_id = max_id(data)
    l_pos = find_pos(data, l_id)
    while l_id > 0:
        for fsi, _ in filter(lambda x: x[1][0] is None and x[0] < l_pos, enumerate(data)):
            if fits(data[l_pos], data[fsi]):
                subst(l_pos, fsi)
                break
        l_id -= 1
        l_pos = find_pos(data, l_id)
    c, vpos = 0, 0
    for i in range(len(data)):
        if data[i][0] != None:
            for j in range(vpos, vpos + data[i][1]):
                c += data[i][0] * j
        vpos += data[i][1]
    return c

t = "233313312141413140211"
print(p2(t))

# correct - 6304576012713
# correct - 6304576012713
