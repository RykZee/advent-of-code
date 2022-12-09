from rope import get_number_of_positions
from os import path

EXAMPLE = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()


def test_get_number_of_positions_example():
    assert get_number_of_positions(EXAMPLE) == 13


def test_get_number_of_positions():
    real_input = _read_file("input")
    assert get_number_of_positions(real_input) == 6181


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
