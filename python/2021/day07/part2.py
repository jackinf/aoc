if __name__ == '__main__':
    with open('input.txt') as f:
        nums = [int(num) for num in f.readline().split(',')]
    print(nums)

    scores = [0] * len(nums)

    for i in range(len(scores)):
        for num in nums:
            n = abs(num - i)
            steps = (n**2 + n) // 2
            scores[i] += steps

    res = min(scores)
    print(f'Result 2: {res}')
