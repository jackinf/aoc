if __name__ == '__main__':
    with open('input.txt') as f:
        nums = [int(num) for num in f.readline().split(',')]
    print(nums)

    scores = [0] * len(nums)

    for i in range(len(scores)):
        for num in nums:
            scores[i] += abs(num - i)

    res = min(scores)
    print(f'Result 1: {res}')
