if __name__ == '__main__':
    with open('sample.txt') as f:
        lines = [line.strip() for line in f]
    print(lines)
