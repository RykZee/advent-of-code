def get_number_of_positions(raw_string):
    head = [0, 0]
    tail = [0, 0]

    tail_positions = set()

    for line in raw_string.splitlines():
        direction, steps = line.split(" ")
        steps = int(steps)
        for index in range(steps):
            if direction == "R":
                head[0] += 1
            if direction == "D":
                head[1] -= 1
            if direction == "L":
                head[0] -= 1
            if direction == "U":
                head[1] += 1

            in_vicinity = tail_in_vicinity_of_head(head, tail)

            if not in_vicinity:
                new_tail_position = get_new_tail_position(head, tail)
                tail[0] = new_tail_position[0]
                tail[1] = new_tail_position[1]

            tail_positions.add(tuple(tail))

    return len(tail_positions)


def tail_in_vicinity_of_head(head, tail):
    vicinity = possible_positions_in_vicinity(head, allow_diagonal=True)
    return tuple(tail) in vicinity


def get_new_tail_position(head, tail):
    possible_new_tail_positions = possible_positions_in_vicinity(tail, True)
    valid_new_tail_positions = possible_positions_in_vicinity(head)
    return possible_new_tail_positions.intersection(valid_new_tail_positions).pop()


def possible_positions_in_vicinity(coordinate, allow_diagonal=False):
    return (
        set(
            [
                tuple([coordinate[0] - 1, coordinate[1] + 0]),
                tuple([coordinate[0] + 1, coordinate[1] + 0]),
                tuple([coordinate[0] + 0, coordinate[1] + 1]),
                tuple([coordinate[0] + 0, coordinate[1] - 1]),
                tuple([coordinate[0], coordinate[1]]),
            ]
        )
        if not allow_diagonal
        else set(
            [
                tuple([coordinate[0] - 1, coordinate[1] + 0]),
                tuple([coordinate[0] + 1, coordinate[1] + 0]),
                tuple([coordinate[0] + 0, coordinate[1] + 1]),
                tuple([coordinate[0] + 0, coordinate[1] - 1]),
                tuple([coordinate[0] - 1, coordinate[1] + 1]),
                tuple([coordinate[0] - 1, coordinate[1] - 1]),
                tuple([coordinate[0] + 1, coordinate[1] + 1]),
                tuple([coordinate[0] + 1, coordinate[1] - 1]),
                tuple([coordinate[0], coordinate[1]]),
            ]
        )
    )
