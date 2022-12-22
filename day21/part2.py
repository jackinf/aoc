if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    def dfs(curr, dd, res):
        if curr in res:
            return res[curr]

        s1, s2, op = dd[curr]
        r1 = dfs(s1, dd, res)
        r2 = dfs(s2, dd, res)

        if curr == "root":
            r1s, r2s = str(r1), str(r2)
            for i in range(len(r1s)):
                if r1s[i] != r2s[i]:
                    print(f'diff at {i}, common part: {r1s[:i]}')
                    break

            delta = abs(r1) - abs(r2)
            best_r1 = 122624242279032
            best_delta = abs(best_r1) - abs(r2)

            print(f'Delta {delta} vs Best delta {best_delta}')

            if r1 > r2:
                return 1
            if r1 < r2:
                return -1
            return 0

        match op:
            case "+": res[curr] = r1 + r2
            case "-": res[curr] = r1 - r2
            case "*": res[curr] = r1 * r2
            case "/": res[curr] = r1 // r2
            case _: raise Exception("no")

        return res[curr]

    def run(guess):
        print("\rPointer", guess, end=' ')
        dd = {}
        res = {}

        for line in lines:
            if len(line) == 17:
                items = line.split(' ')
                target, source1, op, source2 = items
                dd[target[:4]] = (source1, source2, op)
            else:
                items = line.split(' ')
                target, numstr = items
                res[target[:4]] = int(numstr)

        res["humn"] = guess

        part2 = dfs("root", dd, res)
        if part2 == 1:
            print('too high')
        elif part2 == -1:
            print('too low')
        else:
            print(f'Result 2: {guess}')

    """
    I have manually found this number by trial and error xD
    
    To automate this properly, start from magic number 3_000_000_000_000
    Then increase 2nd index of number till r1 - r2 is negative -> if it is, then revert the number.
    Continue increasing each following index.
    Finish when r1 - r2 = 0.
    """
    guess = 3_353_687_996_514

    run(guess)  # todo: implement the above-mentioned algorithm

