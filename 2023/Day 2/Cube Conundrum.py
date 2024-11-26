from math import prod


def check_game_possibility(line):
    red = 12
    green = 13
    blue = 14
    max_values = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    l = ['red', 'green', 'blue']
    game = line.split(":")[0].split(" ")[-1]
    rest_of_line = line.strip().split(":")[-1].strip().split(" ")
    game_val = int(game)
    last_d = None
    game_hash = {

    }
    for indx, char in enumerate(rest_of_line):
        if char.isdigit():
            last_d = int(char)
        else:
            if 'green' in char:
                # if last_d and last_d > max_values['green']:
                #     game_val = 0
                #     break
                game_hash['green'] = max(game_hash.get('green', 0), last_d)
            elif 'red' in char:
                # if last_d and last_d > max_values['red']:
                #     game_val = 0
                #     break
                game_hash['red'] = max(game_hash.get('red', 0), last_d)

            elif 'blue' in char:
                # if last_d and last_d > max_values['blue']:
                #     game_val = 0
                #     break
                game_hash['blue'] = max(game_hash.get('blue', 0), last_d)
    print(f"game val {game_val}")

    prod(game_hash.values())

    # return game_val
    return prod(game_hash.values())



def sum_of_possible_games():
    total_of_game_ids = 0
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            total_of_game_ids += check_game_possibility(line.strip())

    return total_of_game_ids


if __name__ == "__main__":
    print(sum_of_possible_games())
