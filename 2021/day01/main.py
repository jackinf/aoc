if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [int(num.strip()) for num in f]
    print(numbers)

    def count_increases(numbers_):
        increases = 0
        for i in range(1, len(numbers_)):
            if numbers_[i] > numbers_[i-1]:
                increases += 1
        return increases

    print(f'Result 1: {count_increases(numbers)}')

    numbers2 = numbers[:] + [0, 0]
    sums = numbers[:]
    for i in range(2, len(numbers2)):
        sums[i-2] += numbers2[i-1]
        sums[i-2] += numbers2[i]
    sums = sums[:-2]

    print(f'Result 2: {count_increases(sums)}')
