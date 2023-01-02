if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [int(num.strip()) for num in f]

    def count_increases(numbers_):
        return sum(1 for n1, n2 in zip(numbers_, numbers_[1:]) if n1 < n2)

    print(f'Result 1: {count_increases(numbers)}')

    sums = numbers[:]
    for i in range(len(numbers) - 2):
        sums[i] += numbers[i + 1]
        sums[i] += numbers[i + 2]
    sums = sums[:-2]

    print(f'Result 2: {count_increases(sums)}')
