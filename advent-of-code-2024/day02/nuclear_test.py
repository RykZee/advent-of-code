from os import path

from nuclear import safe_reports, safe_reports_with_dampener

EXAMPLE = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()


def test_safe_reports_example():
  actual = safe_reports(EXAMPLE)
  assert actual == 2


def test_safe_reports():
  actual = safe_reports(_read_file("input"))
  assert actual == 257


def test_safe_reports_dampener_example():
  actual = safe_reports_with_dampener(EXAMPLE)
  assert actual == 4


def test_safe_reports_dampener():
  actual = safe_reports_with_dampener(_read_file("input"))
  assert actual == 328


def _read_file(filename: str):
  dir_path = path.dirname(path.realpath(__file__))
  with open(f"{dir_path}/{filename}", "r") as f:
    return f.read().strip()
