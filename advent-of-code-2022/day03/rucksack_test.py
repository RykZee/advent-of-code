from rucksack import badge, get_priorities
from os import path

EXAMPLE_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_priority_example():
    assert get_priorities(EXAMPLE_INPUT) == 157


def test_priority():
    test_input = _read_file("input")
    assert get_priorities(test_input) == 7990


def test_badge_example():
    assert badge(EXAMPLE_INPUT) == 70


def test_badge():
    test_input = _read_file("input")
    assert badge(test_input) == 2602


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
