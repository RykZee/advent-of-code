import re


def unscramble_memory(text: str) -> int:
    mul_instructions = _get_mul_instructions(text)

    return mul_instructions


def _get_mul_instructions(text: str) -> int:
    regex = r"mul\((\d+),(\d+)\)"
    result = 0
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        matches = re.findall(regex, line)
        for match in matches:
            result += (int(match[0]) * int(match[1]))
    return result
