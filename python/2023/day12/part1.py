with open('input.txt', 'r') as f:
    lines = [(list(group[0]), list(map(int, group[1].split(',')))) for group in [line.split() for line in f.read().split('\n')]]


acc = set()
def dfs(arr, ptr, counter):
    global acc
    if len(arr) == ptr:
        gaps = [len(val) for val in ''.join(arr).split('.') if len(val) > 0]
        if gaps == counter:
            acc.add(''.join(arr))
        return

    if arr[ptr] in {'#', '.'}:
        dfs(arr, ptr + 1, counter)
    elif arr[ptr] == '?':
        arr[ptr] = '#'
        dfs(arr, ptr, counter)
        arr[ptr] = '.'
        dfs(arr, ptr, counter)
        arr[ptr] = '?'


results = []
for i, (arrangement, counter) in enumerate(lines):
    acc = set()
    dfs(arrangement, 0, counter)
    results.append(len(acc))

print(sum(results))