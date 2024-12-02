import math

with open('input.txt', 'r') as f:
    text = f.read().split('\n')
    total_times = list(map(int, text[0].split(':')[1].split()))
    distances = list(map(int, text[1].split(':')[1].split()))
    assert len(total_times) == len(distances)

wins = [0] * len(total_times)
for i, (total_time, record_distance) in enumerate(zip(total_times, distances)):
    for wait_time in range(1, total_time):
        if (total_time - wait_time) * wait_time > record_distance:
            wins[i] += 1

print(f'Total: {math.prod(wins)}')
