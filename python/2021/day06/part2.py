# (days_left, timer) => fish will be produced
cache = {}


def dfs(days_left, timer):
    key = (days_left, timer)
    if key in cache:
        return cache[key]

    if days_left == 0:
        return 0

    new_timer = timer - 1
    if new_timer == -1:
        # timer reset, new fish created
        res = dfs(days_left - 1, 6) + dfs(days_left - 1, 8) + 1
    else:
        res = dfs(days_left - 1, new_timer)

    cache[key] = res
    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [int(num) for num in f.readline().split(',')]

    final_res = len(numbers)
    for num in numbers:
        final_res += dfs(256, num)

    print(f'Result 2: {final_res}')
