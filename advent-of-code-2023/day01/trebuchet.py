def trebuchet(text):
    result = 0
    for line in text.split("\n"):
        digits = list(filter(lambda x: x.isnumeric(), line))
        if digits:
            result += int(digits[0] + digits[-1])
    return result
