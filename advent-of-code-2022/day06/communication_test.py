from communication import get_marker_from_message
from os import path

EXAMPLE = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""


def test_get_marker_from_message_example():
    actual = get_marker_from_message(EXAMPLE)
    assert actual[0] == 7
    assert actual[1] == 5
    assert actual[2] == 6
    assert actual[3] == 10
    assert actual[4] == 11


def test_get_marker_from_message():
    test_input = _read_file("input")
    assert get_marker_from_message(test_input)[0] == 1802


def test_get_marker_from_message_with_limit_example():
    actual = get_marker_from_message(EXAMPLE, limit=14)
    assert actual[0] == 19
    assert actual[1] == 23
    assert actual[2] == 23
    assert actual[3] == 29
    assert actual[4] == 26


def test_get_marker_from_message_with_limit():
    test_input = _read_file("input")
    actual = get_marker_from_message(test_input, limit=14)
    assert actual[0] == 3551


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
