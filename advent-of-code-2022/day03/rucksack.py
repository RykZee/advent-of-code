def get_priorities(items):
    points = 0

    for line in iter(items.splitlines()):
        if line == "":
            continue

        half = len(line) // 2
        first_half = set(line[:half])
        second_half = set(line[half:])

        char_in_common = first_half.intersection(second_half).pop()
        ascii_number = ord(char_in_common)
        if 97 <= ascii_number <= 122:
            points += ascii_number - 96
        else:
            points += ascii_number - 38

    return points


def badge(items):
    points = 0
    items_list = [item for item in iter(items.splitlines()) if item != ""]
    for one, two, three in _three_at_a_time(items_list):
        char_in_common = _intersection_of(one, two, three).pop()
        ascii_number = ord(char_in_common)
        if 97 <= ascii_number <= 122:
            points += ascii_number - 96
        else:
            points += ascii_number - 38

    return points


def _intersection_of(one, two, three):
    return set(one).intersection(set(two).intersection(set(three)))


def _three_at_a_time(items):
    return zip(*[iter(items)] * 3)
