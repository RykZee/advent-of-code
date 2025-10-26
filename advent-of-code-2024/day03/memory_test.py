from os import path
from memory import unscramble_memory

EXAMPLE = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip()

EXAMPLE2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()


def test_unscramble_memory_example():
    actual = unscramble_memory(EXAMPLE)
    assert actual == 161


def test_safe_reports():
    actual = unscramble_memory(_read_file("input"))
    assert actual == 174103751


def test_safe_reports_with_more_instructions_example():
    actual = unscramble_memory(EXAMPLE2, use_mode=True)
    assert actual == 48


def test_safe_reports_with_more_instructions():
    actual = unscramble_memory(_read_file("input"), use_mode=True)
    assert actual == 100411201


def _read_file(filename: str):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read().strip()
