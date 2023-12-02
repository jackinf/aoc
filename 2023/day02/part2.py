with open('input.txt') as f:
    lines = f.read().split('\n')
    games_arr = [[x for x in line.split(':')] for line in lines]

games = {}
game_powers = {}
for game_arr in games_arr:
    game = {}
    game_name = game_arr[0].strip()
    game_id = int(game_name.split()[1])
    group_arrs = game_arr[1].strip().split(';')

    for group_arr in group_arrs:
        for num_col_arr in group_arr.split(','):
            num_col = num_col_arr.split()
            amount = int(num_col[0].strip())
            color = num_col[1].strip()

            if color not in game:
                game[color] = amount
            else:
                game[color] = max(game[color], amount)

    games[game_id] = game
    game_powers[game_id] = game.get('blue', 1) * game.get('green', 1) * game.get('red', 1)

game_powers_total = sum(game_powers.values())
