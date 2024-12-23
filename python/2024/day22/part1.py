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

def simulate(secret: int, steps: int) -> int:
    res = secret
    for i in range(steps):
        res = step(res)
    return res

def run():
    lines = read_input('input.txt')
    final_result = 0

    for secret in lines:
        final_result += simulate(secret, 2000)

    print(f'Part 1: {final_result}')

def example():
    res = 1
    for i in range(2000):
        res = step(res)

if __name__ == '__main__':
    run()