from supply import supply_stacks
from os import path

STACK_EXAMPLE = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
"""

EXAMPLE_MOVES = """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


STACK = """
    [H]         [H]         [V]
    [V]         [V] [J]     [F] [F]
    [S] [L]     [M] [B]     [L] [J]
    [C] [N] [B] [W] [D]     [D] [M]
[G] [L] [M] [S] [S] [C]     [T] [V]
[P] [B] [B] [P] [Q] [S] [L] [H] [B]
[N] [J] [D] [V] [C] [Q] [Q] [M] [P]
[R] [T] [T] [R] [G] [W] [F] [W] [L]
 1   2   3   4   5   6   7   8   9
"""


def test_supply_stacks_example():
    assert supply_stacks(STACK_EXAMPLE, EXAMPLE_MOVES) == "CMZ"


def test_supply_stacks():
    moves = _read_file("input")
    assert supply_stacks(STACK, moves) == "HBTMTBSDC"


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
