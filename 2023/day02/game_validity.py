data_file = open("input.txt", "r")
games = data_file.read().split("\n")
data_file.close()


def puzzle1():
    limits = {"red": 12, "green": 13, "blue": 14}
    sum_valid_ids = 0

    for i, game in enumerate(games):
        is_valid = True
        rounds = game.split(": ")[1]
        rounds = rounds.split("; ")

        for round in rounds:
            cubes = round.split(", ")
            cubes = map(lambda cube: cube.split(), cubes)
            for cube in cubes:
                if int(cube[0]) > limits[cube[1]]:
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            sum_valid_ids += i + 1

    print(sum_valid_ids)


def puzzle2():
    from functools import reduce

    sum_game_powers = 0

    for i, game in enumerate(games):
        game_mins = {"red": 0, "green": 0, "blue": 0}

        rounds = game.split(": ")[1]
        rounds = rounds.split("; ")

        for round in rounds:
            cubes = round.split(", ")
            cubes = list(map(lambda cube: cube.split(), cubes))
            for cube in cubes:
                game_mins[cube[1]] = max(int(cube[0]), game_mins[cube[1]])

        sum_game_powers += reduce(lambda x, y: x * y, game_mins.values())

    print(sum_game_powers)


puzzle2()
