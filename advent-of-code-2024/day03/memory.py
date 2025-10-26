import re
from enum import StrEnum


class Mode(StrEnum):
    DO = "DO"
    DO_NOT = "DO_NOT"


def unscramble_memory(text: str, use_mode: bool = False) -> int:
    mul_instructions = _get_mul_instructions(text)

    calculations = _calculate(mul_instructions, use_mode=use_mode)
    return calculations


def _get_mul_instructions(text: str) -> list[str]:
    regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    result = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        matches = re.findall(regex, line)
        result.extend(matches)
    return result


def _calculate(instructions: list[str], use_mode: bool = False) -> int:
    regex = r"\d+"
    current_mode = Mode.DO

    result = 0
    for instruction in instructions:
        if instruction.startswith("mul"):
            if _should_add(use_mode, current_mode):
                matches = re.findall(regex, instruction)
                result += int(matches[0]) * int(matches[1])
        elif instruction == "don't()":
            current_mode = Mode.DO_NOT
        elif instruction == "do()":
            current_mode = Mode.DO
    return result


def _should_add(use_mode: bool, mode: Mode) -> bool:
    if not use_mode:
        return True
    return mode == Mode.DO
