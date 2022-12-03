def get_priorities(items):
    points = 0

    for line in iter(items.splitlines()):
        if line == "":
            continue

        half = len(line) // 2
        first_half = set(line[:half])
        second_half = set(line[half:])

        common_chars = first_half.intersection(second_half)
        for char in common_chars:
            if 97 <= ord(char) <= 122:
                points += ord(char) - 96
            else:
                points += ord(char) - 38

    return points


def badge(items):
    points = 0
    items_list = [item for item in iter(items.splitlines()) if item != ""]
    for one, two, three in zip(*[iter(items_list)] * 3):
        common_chars = set(one).intersection(set(two).intersection(set(three)))
        if len(common_chars) > 1:
            breakpoint()
        for char in common_chars:
            if 97 <= ord(char) <= 122:
                points += ord(char) - 96
            else:
                points += ord(char) - 38

    return points
