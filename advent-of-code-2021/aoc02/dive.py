def dive_part_1(move_values):
    distance = 0
    depth = 0
    for value in move_values:
        if "" == value:
            continue
        direction, move = value.split(" ")
        move = int(move)
        if "forward" == direction:
            distance += move
        elif "down" == direction:
            depth += move
        elif "up" == direction:
            depth -= move
    return distance, depth


def dive_part_2(move_values):
    distance = 0
    depth = 0
    aim = 0
    for value in move_values:
        if "" == value:
            continue
        direction, move = value.split(" ")
        move = int(move)
        if "forward" == direction:
            distance += move
            depth += aim * move
        elif "down" == direction:
            aim += move
        elif "up" == direction:
            aim -= move
    return distance, depth
