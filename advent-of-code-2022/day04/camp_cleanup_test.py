from camp_cleanup import get_overlapping_sections
from os import path

INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_completely_overlapping_sections_example():
    actual, _ = get_overlapping_sections(INPUT)
    assert actual == 2


def test_completely_overlapping_sections():
    test_input = _read_file("input")
    actual, _ = get_overlapping_sections(test_input)
    assert actual == 576


def test_any_overlapping_sections_example():
    _, actual = get_overlapping_sections(INPUT)
    assert actual == 4


def test_any_overlapping_sections():
    test_input = _read_file("input")
    _, actual = get_overlapping_sections(test_input)
    assert actual == 905


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
