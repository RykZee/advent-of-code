from trebuchet import trebuchet, trebuchet2
from os import path

first_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

second_input = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

third_input = """
sevenfiveonesevenfjccpmnnninesix3nine
"""


def test_trebuchet_sample():
    assert trebuchet(first_input) == 142


def test_trebuchet():
    test_input = _read_file("input")
    assert trebuchet(test_input) == 52974


def test_trebuchet2_sample():
    assert trebuchet2(second_input) == 281


def test_trebuchet2():
    test_input = _read_file("input")
    assert trebuchet2(test_input) == 53340


def test_trebuchet2_multiple_entries():
    assert trebuchet2(third_input) == 79


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
