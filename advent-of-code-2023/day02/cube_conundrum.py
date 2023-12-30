LIMITS = {"red": 12, "green": 13, "blue": 14}


def possible_games(puzzle):
    parsed = _parse(puzzle)

    result = 0
    for game_id, game in parsed.items():
        if _is_possible(game):
            result += game_id
    return result


def _parse(puzzle):
    result = {}
    for index, line in enumerate(puzzle.split("\n")):
        game = line.split(":")[1].split(";")
        game_id = index+1
        result[game_id] = []
        for takes in game:
            parsed = {"red": 0, "green": 0, "blue": 0}
            take = takes.split(",")
            for value in take:
                number, color = value.strip().split(" ")
                parsed[color] += int(number)
            result[game_id].append(parsed)
    return result

def _is_possible(game):
    for take in game:
        for color, quantity in take.items():
            if LIMITS[color] < quantity:
                return False
    return True
