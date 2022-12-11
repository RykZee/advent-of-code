from monkey import do_monkey_business
from os import path


def test_do_monkey_business_example():
    example_input = _read_file("example_input")
    assert do_monkey_business(example_input) == 10_605


def test_do_monkey_business():
    test_input = _read_file("input")
    assert do_monkey_business(test_input) == 56_595


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
