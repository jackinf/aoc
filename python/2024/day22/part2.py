def read_input(file_name: str):
    with open(file_name) as f:
        return list(map(int, f.read().split('\n')))

def mix(num: int, secret: int) -> int:
    return num ^ secret

def prune(num: int):
    return num % 16777216

def step(secret: int) -> int:
    secret ^= secret * 64
    secret %= 16777216

    secret ^= secret // 32
    secret %= 16777216

    secret ^= secret * 2048
    secret %= 16777216

    return secret

def simulate(secret: int, steps: int):
    last_digit = lambda x: int(str(x)[-1])

    prices = [last_digit(secret)]
    changes = [None]
    patterns = {}

    for i in range(steps):
        secret = step(secret)
        prices.append(last_digit(secret))
        changes.append(prices[-1] - prices[-2])

    prices.pop(0)
    changes.pop(0)

    for i in range(len(changes) - 3):
        pattern = (changes[i], changes[i+1], changes[i+2], changes[i+3])
        if pattern not in patterns:
            patterns[pattern] = prices[i+3]

    return prices, changes, patterns

def run():
    lines = read_input('input.txt')

    all_patterns = []
    all_pattern_keys = set()
    for secret in lines:
        prices, changes, patterns = simulate(secret, 2000)
        all_patterns.append(patterns)
        for key in patterns.keys():
            all_pattern_keys.add(key)

    best_score = 0

    for attempt in all_pattern_keys:
        print(attempt)
        score = 0
        for pattern in all_patterns:
            score += pattern.get(attempt, 0)

        best_score = max(best_score, score)

    print(f'Part 2: {best_score}')  # 1877 - too high

def example():
    res = 1
    for i in range(2000):
        res = step(res)

if __name__ == '__main__':
    run()