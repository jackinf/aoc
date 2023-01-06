from pprint import pprint


def solve(boards):
    callouts = set()

    for number in numbers:
        callouts.add(number)

        for i, board in enumerate(boards):
            for x in range(5):
                row_matches = sum(1 for j in range(5) if board[j][x] in callouts)
                if row_matches == 5:
                    return board, number, callouts

                col_matches = sum(1 for j in range(5) if board[x][j] in callouts)
                if col_matches == 5:
                    return board, number, callouts


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        line0 = lines.pop(0)
        numbers = [int(x) for x in line0.split(',')]

    boards = []

    while lines:
        lines.pop(0)
        board = []
        for _ in range(5):
            board.append([int(x) for x in lines.pop(0).split()])
        boards.append(board)

    board, number, callouts = solve(boards)
    other_nums = sum(x for y in board for x in y if x not in callouts)
    print(f'Result 1: {other_nums * number}')
