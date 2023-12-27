from trebuchet import trebuchet
from os import path

first_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()


def test_trebuchet_sample():
    assert trebuchet(first_input) == 142


def test_trebuchet():
    test_input = _read_file("input")
    assert trebuchet(test_input) == 52974


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
