with open('input.txt', 'r') as f:
    histories = f.read().split('\n')
    histories = [list(map(int, history.split())) for history in histories]

searched_values = []
for history in histories:
    collection = [history[:]]

    # Step 1. create subsequences
    while not all(x == 0 for x in collection[-1]):
        seq = []
        for i in range(len(collection[-1]) - 1):
            diff = collection[-1][i + 1] - collection[-1][i]
            seq.append(diff)
        collection.append(seq)

    # Step 2. Find value by calculating last number of each step. Do it in reverse
    for i in range(len(collection) - 1, 0, -1):
        new_val = collection[i][-1] + collection[i - 1][-1]
        collection[i - 1].append(new_val)

    searched_values.append(collection[0][-1])

total_result = sum(searched_values)
print(f'Part 1: {total_result}')