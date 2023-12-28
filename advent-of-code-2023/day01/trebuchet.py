import re

VALID_VALUES = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def trebuchet(text):
    result = 0
    for line in text.split("\n"):
        numerics_map = _get_numeric_chars_with_index_at(line)
        digits = _sorted_numerics_list_from_map(numerics_map)
        if digits:
            result += int(digits[0] + digits[-1])
    return result


def trebuchet2(text):
    result = 0
    for line in text.split("\n"):
        digits = _find_digits(line)
        if digits:
            result += int(digits[0] + digits[-1])
    return result


def _find_digits(string):
    result = _get_numeric_chars_with_index_at(string)
    for valid_value in VALID_VALUES:
        if valid_value in string:
            matches = [m.start() for m in re.finditer(valid_value, string)]
            for match in matches:
                result[match] = VALID_VALUES[valid_value]
    return _sorted_numerics_list_from_map(result)


def _get_numeric_chars_with_index_at(string):
    result = {}
    for index, char in enumerate(string):
        if char.isnumeric():
            result[index] = str(char)
    return result


def _sorted_numerics_list_from_map(numerics_map):
    return [v for k, v in sorted(numerics_map.items())]
