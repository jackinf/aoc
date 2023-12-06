with open('input.txt', 'r') as f:
    text = f.read().split('\n')
    total_time = int(''.join(text[0].split(':')[1].split()))
    record_distance = int(''.join(text[1].split(':')[1].split()))

distances = [(total_time - wait_time) * wait_time for wait_time in range(1, total_time)]
wins = sum((1 for distance in distances if distance > record_distance))

print(f'Part 2: {wins}')
