from os import path
from xmas import find_xmas_hits

EXAMPLE = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()


def test_find_xmas_example():
    actual = find_xmas_hits(EXAMPLE)
    assert actual == 18


def test_find_xmas():
    actual = find_xmas_hits(_read_file("input"))
    assert actual == 2406


def _read_file(filename: str):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read().strip()
