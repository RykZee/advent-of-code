from os import path
from treetop import get_visibility, get_scenic_score


EXAMPLE = """
30373
25512
65332
33549
35390
"""[
    1:
]


def test_get_visibility_example():
    assert get_visibility(EXAMPLE) == 21


def test_get_visibility():
    test_input = _read_file("input")
    assert get_visibility(test_input) == 1849


def test_get_scenic_score_example():
    assert get_scenic_score(EXAMPLE) == 8


def test_get_scenic_score():
    test_input = _read_file("input")
    assert get_scenic_score(test_input) == 201600


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
