from os import path
from guard import guard_path

EXAMPLE = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()


def test_guard_path_example():
    actual = guard_path(EXAMPLE)
    assert actual == 41


def test_guard_path():
    actual = guard_path(_read_file("input"))
    assert actual == 6505


def _read_file(filename: str):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read().strip()
