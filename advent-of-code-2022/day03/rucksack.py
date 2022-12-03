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

