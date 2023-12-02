with open('input.txt') as f:
    lines = f.read().split('\n')
    games_arr = [[x for x in line.split(':')] for line in lines]

valid_games = []
for game_arr in games_arr:
    game = {}
    game_name = game_arr[0].strip()
    game_id = int(game_name.split()[1])
    group_arrs = game_arr[1].strip().split(';')

    valid = True
    for group_arr in group_arrs:
        for num_col_arr in group_arr.split(','):
            num_col = num_col_arr.split()
            amount = int(num_col[0].strip())
            color = num_col[1].strip()
            game[color] = game.get(color, 0) + amount

            valid_red = color == 'red' and amount <= 12
            valid_green = color == 'green' and amount <= 13
            valid_blue = color == 'blue' and amount <= 14
            if not (valid_red or valid_green or valid_blue):
                valid = False

    if valid:
        valid_games.append(game_id)

valid_games_total = sum(valid_games)

print(valid_games)
print(valid_games_total)