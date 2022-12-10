from ctr import get_signal_strength, get_render_image
from os import path

EXAMPLE_RENDER = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
""".strip()

RENDERED_IMAGE = """
####.####.####..##..#..#...##..##..###..
#.......#.#....#..#.#..#....#.#..#.#..#.
###....#..###..#....####....#.#..#.###..
#.....#...#....#....#..#....#.####.#..#.
#....#....#....#..#.#..#.#..#.#..#.#..#.
####.####.#.....##..#..#..##..#..#.###..
""".strip()


def test_get_signal_strength_example():
    example = _read_file("example_input")
    actual = get_signal_strength(example)
    assert actual[0] == 420
    assert actual[1] == 1140
    assert actual[2] == 1800
    assert actual[3] == 2940
    assert actual[4] == 2880
    assert actual[5] == 3960
    assert sum(actual) == 13_140


def test_get_signal_strength():
    test_input = _read_file("input")
    assert sum(get_signal_strength(test_input)) == 13180


def test_render_image_example():
    example = _read_file("example_input")
    assert get_render_image(example) == EXAMPLE_RENDER


def test_render_image():
    example = _read_file("input")
    actual = get_render_image(example)
    assert actual == RENDERED_IMAGE


def _read_file(filename):
    dir_path = path.dirname(path.realpath(__file__))
    with open(f"{dir_path}/{filename}", "r") as f:
        return f.read()
