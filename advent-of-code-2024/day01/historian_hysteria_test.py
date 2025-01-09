from historian_hysteria import find_differences
from os import path

EXAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()


def test_difference_example():
    left, right = _split_to_two_lists(EXAMPLE_INPUT)
    actual = find_differences(left, right)
    assert actual == 11


def test_difference_test():
  left, right = _split_to_two_lists(_read_file("test_input"))
  actual = find_differences(left, right)
  assert actual == 1651298


def _split_to_two_lists(text):
    left = []
    right = []
    for line in text.split("\n"):
        first, second = line.split()
        left.append(int(first))
        right.append(int(second))
    return left, right


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read().strip()
