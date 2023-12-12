"""
Thought process

???.### 1,1,3

.??.### 1,1,3
..?.### 1,1,3
....### 1,1,0 -> +0
backtrack
..#.### 1,0,0 -> +0
backtrack
#.#.### 0,0,0 -> +1

def backtrack(arr, counter, arr_pointer, counter_pointer)
    - base-case: if all numbers are 0 AND no question marks (AND non-empty input string)
    - if arr_pointer == len(arr):
        - if len(counter) == counter_pointer: return 1
        - else: return 0

    - optimization:
        if tuple(counter[counter_pointer:] + arr[arr_pointer:]) in seen:
            return seen[tuple(arr + [str])]

    - subresult1, subresult2 = 0, 0
    - '.' or '?' case:
        - recurse into next subproblem(arr, counter, arr_pointer + 1, counter_pointer) => subresult1

    - '#' or '?' case:
        - if counter[counter_pointer] value is 1:
            - we can ignore decreasing counter because we'd have to restore the value, and left-side will be ignored anyways
            - recurse into next subproblem(arr[I+1:], counter, counter_pointer + 1) => subresult2
        - else:
            - counter[counter_pointer] -= 1
            - recurse into next subproblem(arr[I+1:], counter, counter_pointer) => subresult2
            - counter[counter_pointer] += 1

    - return subresult1 + subresult2
"""

with open('sample.txt', 'r') as f:
    lines = [(list(group[0]), list(map(int, group[1].split(',')))) for group in [line.split() for line in f.read().split('\n')]]


def backtrack(arr, counter, arr_pointer, counter_pointer, acc, cache):
    # base case
    if len(arr) == arr_pointer:
        # print(''.join(arr), counter)
        if all(val == 0 for val in counter):
            acc.add(''.join(arr))
        return
    if len(counter) == counter_pointer:
        return

    if arr[arr_pointer] == '#':
        # are we out of moves
        if counter[counter_pointer] > 0:
            counter[counter_pointer] -= 1
            inc = 1 if counter[counter_pointer] == 0 else 0
            backtrack(arr, counter, arr_pointer + 1, counter_pointer + inc, acc, cache)
            counter[counter_pointer] += 1

    elif arr[arr_pointer] == '.' and counter[counter_pointer] == 0:
        backtrack(arr, counter, arr_pointer + 1, counter_pointer, acc, cache)

    elif arr[arr_pointer] == '?':
        if counter[counter_pointer] > 0:
            counter[counter_pointer] -= 1
            inc = 1 if counter[counter_pointer] == 0 else 0
            backtrack(arr, counter, arr_pointer + 1, counter_pointer + inc, acc, cache)
            counter[counter_pointer] += 1

        # .-case
        symbol, arr[arr_pointer] = arr[arr_pointer], '.'
        backtrack(arr, counter, arr_pointer + 1, counter_pointer, acc, cache)
        arr[arr_pointer] = symbol


results = []
cache = {}
for arrangement, counter in lines[:1]:
    # print('===')
    print(''.join(arrangement))
    acc = set()
    backtrack(arrangement, counter, 0, 0, acc, cache)
    print(acc)
    results.append(len(acc))

print(results)
total_result = sum(results)
print(f'Part 1: {total_result}')