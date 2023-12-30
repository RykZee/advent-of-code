def possible_games(puzzle):
    parsed_puzzle = _parse(puzzle)
    print(parsed_puzzle)


def _parse(puzzle):
    for line in puzzle.split("\n"):
        games = line.split(":")[1].split(";")
        for game in games:
            values = game.split(",")
            for value in values:
                value.strip()
                breakpoint()
