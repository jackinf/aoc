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


def backtrack(arr, counter, arr_pointer, counter_pointer, cache):
    # base case
    if len(arr) <= arr_pointer:
        return 1 if len(counter) == counter_pointer else 0
    if len(counter) <= counter_pointer:
        return 0

    # optimization
    if tuple(counter[counter_pointer:] + arr[arr_pointer:]) in cache:
        return cache[tuple(arr + [str])]

    subresult1, subresult2 = 0, 0
    if arr[arr_pointer] in {'.', '?'}:
        subresult1 = backtrack(arr, counter, arr_pointer + 1, counter_pointer, cache)

    if arr[arr_pointer] in {'#', '?'}:
        if counter[counter_pointer] == 1:
            # move pointer 2 steps because if last '#' ends, then next is guaranteed '.'
            subresult2 = backtrack(arr, counter, arr_pointer + 2, counter_pointer + 1, cache)
        else:
            counter[counter_pointer] -= 1
            subresult2 = backtrack(arr, counter, arr_pointer + 1, counter_pointer, cache)
            counter[counter_pointer] += 1

    return subresult1 + subresult2

results = []
cache = {}
for arrangement, counter in lines:
    result = backtrack(arrangement, counter, 0, 0, cache)
    results.append(result)

print(results)
total_result = sum(results)
print(f'Part 1: {total_result}')