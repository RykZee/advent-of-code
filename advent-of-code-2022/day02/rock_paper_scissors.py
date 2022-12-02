MAPPER = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

OUTCOME = {
    "rockpaper": "win",
    "rockscissors": "lose",
    "rockrock": "tie",
    "paperpaper": "tie",
    "paperscissors": "win",
    "paperrock": "lose",
    "scissorspaper": "lose",
    "scissorsscissors": "tie",
    "scissorsrock": "win",
}

POINTS = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lose": 0,
    "tie": 3,
    "win": 6,
}


def calculate_score(strategy):
    points = 0
    for line in iter(strategy.splitlines()):
        if line == "":
            continue
        opponent_move, own_move = line.split(" ")
        combination = MAPPER[opponent_move] + MAPPER[own_move]
        outcome = OUTCOME[combination]
        points += POINTS[outcome] + POINTS[MAPPER[own_move]]

    return points
