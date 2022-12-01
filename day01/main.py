if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().split('\n')

    if len([line for line in lines if line.strip()]) == 0:
        print(0)
        exit(0)

    elves = [0]
    for line in lines:
        if line == '':
            elves.append(0)
            continue
        elves[-1] += int(line)
    elves.sort(reverse=True)

    print(f"Result 1: {max(elves)}")

    print(f"Result 2: {sum([x for x in elves][:3])}")
