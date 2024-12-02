if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [int(num) for num in f.readline().split(',')]

    day = 1
    while day <= 80:
        N = len(numbers)
        for i in range(N):
            numbers[i] -= 1
            if numbers[i] == -1:
                numbers[i] = 6
                numbers.append(8)
        day += 1

    print(f'Result 1: {len(numbers)}')