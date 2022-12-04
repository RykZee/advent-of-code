from bingo import get_bingo_score
from os import path

NUMBERS_TO_DRAW_EXAMPLE = [
    7,
    4,
    9,
    5,
    11,
    17,
    23,
    2,
    0,
    14,
    21,
    24,
    10,
    16,
    13,
    6,
    15,
    25,
    12,
    22,
    18,
    20,
    8,
    19,
    3,
    26,
    1,
]

BOARDS = """
22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def test_bingo_example():
    assert get_bingo_score(NUMBERS_TO_DRAW_EXAMPLE, BOARDS) == 4512


NUMBERS_TO_DRAW = [
    63,
    23,
    2,
    65,
    55,
    94,
    38,
    20,
    22,
    39,
    5,
    98,
    9,
    60,
    80,
    45,
    99,
    68,
    12,
    3,
    6,
    34,
    64,
    10,
    70,
    69,
    95,
    96,
    83,
    81,
    32,
    30,
    42,
    73,
    52,
    48,
    92,
    28,
    37,
    35,
    54,
    7,
    50,
    21,
    74,
    36,
    91,
    97,
    13,
    71,
    86,
    53,
    46,
    58,
    76,
    77,
    14,
    88,
    78,
    1,
    33,
    51,
    89,
    26,
    27,
    31,
    82,
    44,
    61,
    62,
    75,
    66,
    11,
    93,
    49,
    43,
    85,
    0,
    87,
    40,
    24,
    29,
    15,
    59,
    16,
    67,
    19,
    72,
    57,
    41,
    8,
    79,
    56,
    4,
    18,
    17,
    84,
    90,
    47,
    25,
]


def test_bingo():
    boards = _read_file("input")
    assert get_bingo_score(NUMBERS_TO_DRAW, boards) == 4512


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
