from dive import dive_part_1, dive_part_2
from os import path

TEST_INPUT = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_dive_with_example():
    actual = dive_part_1(TEST_INPUT)
    assert actual == (15, 10)
    assert actual[0] * actual[1] == 150


def test_dive_part_1():
    file = _read_file("input").split("\n")
    actual = dive_part_1(file)
    assert actual[0] == 1998
    assert actual[1] == 741
    assert actual[0] * actual[1] == 1480518


def test_dive_aim_example():
    actual = dive_part_2(TEST_INPUT)
    assert actual[0] == 15
    assert actual[1] == 60
    assert actual[0] * actual[1] == 900


def test_dive_part_2():
    file = _read_file("input").split("\n")
    actual = dive_part_2(file)
    assert actual[0] == 1998
    assert actual[1] == 642047
    assert actual[0] * actual[1] == 1282809906


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
