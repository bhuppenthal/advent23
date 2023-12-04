def parse_input(games):
    sum = 0

    for game in games:
        game = game.split(':')

        game_info = game[0].split(' ')
        game_id = game_info[-1]

        rounds = game[1].split(';')

        min_red = 0;
        min_green = 0;
        min_blue = 0;

        for round in rounds:
            draws = round.split(', ')

            for draw in draws:
                draw = draw.split(' ')
                draw = [x for x in draw if x]
                if draw[1] == 'red' and int(draw[0]) > min_red:
                    min_red = int(draw[0])
                if draw[1] == 'green' and int(draw[0]) > min_green:
                    min_green = int(draw[0])
                if draw[1] == 'blue' and int(draw[0]) > min_blue:
                    min_blue = int(draw[0])
        sum += min_red*min_green*min_blue

    return sum

with open('input.txt') as f:
    input = f.read().splitlines()
print(parse_input(input))

