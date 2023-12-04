def parse_input(games):
    sum = 0

    for game in games:
        game = game.split(':')

        game_info = game[0].split(' ')
        game_id = game_info[-1]

        rounds = game[1].split(';')

        valid_game = True
        for round in rounds:
            draws = round.split(', ')

            for draw in draws:
                draw = draw.split(' ')
                draw = [x for x in draw if x]
                if draw[1] == 'red' and int(draw[0]) > 12:
                    valid_game = False
                if draw[1] == 'green' and int(draw[0]) > 13:
                    valid_game = False
                if draw[1] == 'blue' and int(draw[0]) > 14:
                    valid_game = False

        if valid_game:
            sum += int(game_id)
    return sum

with open('input.txt') as f:
    input = f.read().splitlines()
print(parse_input(input))

