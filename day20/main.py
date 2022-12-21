from pprint import pprint

import math

if __name__ == '__main__':
    with open('sample.txt') as f:
        numbers = [int(line.strip()) for line in f]
        collection = {order: val for order, val in enumerate(numbers)}
        indexes = [order for order, _ in enumerate(numbers)]

    pprint(indexes)
    sign = lambda x: int(math.copysign(1, x))  # two will work

    """
    1, 2, -3, 3, -2, 0, 4
    
    collection:
    
        ord: val
        ----
        0: 1
        1: 2
        2: -3
        3: 3
        4: -2
        5: 0
        6: 4
    
    arr (indexes of numbers):
        0, 1, 2, 3, 4, 5, 6
        
    from 0 to N:
    steps:
        0: 
            collection[0] = 1
            old: 0, 1, 2, 3, 4, 5, 6
            new: 1, 0, 2, 3, 4, 5, 6
        1:  
            collection[1] = 2
            old: 1, 0, 2, 3, 4, 5, 6
            new: 0, 2, 1, 3, 4, 5, 6
        2:  
            collection[2] = -3
            old: 0, 2, 1, 3, 4, 5, 6
            new: 0, 1, 3, 4, 2, 5, 6
        ...
            
    """

    N = len(indexes)

    for i in range(N):
        print()
        print(f'step #{i}:', end=' ')
        print(', '.join([str(collection[index]) for index in indexes]), end='. ')

        val = collection[i]
        print(f'Moving {i}:{val}', end='. ')

        if val == 0:
            continue

        # if the number is going to do more cycles than there are numbers in the array
        if abs(val) > N:
            val %= N

        index_from = indexes.index(i)
        indexes.pop(index_from)

        # check if value goes out of bounds when positive
        if val > 0 and index_from + val >= N:
            val -= (N-1)

        # check if value goes out of bounds when negative
        elif val < 0 and index_from < abs(val) + 1:
            val = (N-1) - abs(val)

        index_to = index_from + val
        indexes.insert(index_to, i)

        print('After moving: ', end='')
        print(', '.join([str(collection[index]) for index in indexes]), end='. ')

    print()
    numbers = [collection[index] for index in indexes]
    start_from = numbers.index(0)
    x1 = collection[indexes[(start_from + 1000) % N]]
    x2 = collection[indexes[(start_from + 2000) % N]]
    x3 = collection[indexes[(start_from + 3000) % N]]

    print(f'Result 1: {x1} + {x2} + {x3} = {x1 + x2 + x3}')



