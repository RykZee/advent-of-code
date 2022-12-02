from rock_paper_scissors import calculate_score
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


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
