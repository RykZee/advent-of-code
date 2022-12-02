from rock_paper_scissors import calculate_score, calculate_score2
from os import path

EXAMPLE_INPUT = """
A Y
B X
C Z
"""


def test_rock_paper_scissors_example():
    assert calculate_score(EXAMPLE_INPUT) == 15


def test_rock_paper_scissors():
    test_input = _read_file("input")
    result = calculate_score(test_input)
    assert result == 12458


def test_rock_paper_scissors_2_example():
    assert calculate_score2(EXAMPLE_INPUT) == 12


def test_rock_paper_scissors_2():
    test_input = _read_file("input")
    assert calculate_score2(test_input) == 12683


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
