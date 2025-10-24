from enum import StrEnum


class Direction(StrEnum):
  ASCENDING = "ASCENDING"
  DESCENDING = "DESCENDING"
  NOT_SET = "NOT_SET"


def safe_reports(text: str) -> int:
  reports = _text_to_reports(text)

  result = 0
  for report in reports:
    if _is_safe_report(report) == 0:
      result += 1

  return result


def safe_reports_with_dampener(text: str) -> int:
  reports = _text_to_reports(text)

  result = 0
  for report in reports:
    if _is_safe_report(report) == 0:
      result += 1
      continue

    made_safe = False
    for j in range(len(report)):
      reduced = report[:j] + report[j + 1 :]
      if _is_safe_report(reduced) == 0:
        made_safe = True
        break

    if made_safe:
      result += 1

  return result


def _is_safe_report(levels: list[int]) -> int:
  direction = Direction.NOT_SET
  for i, level in enumerate(levels):
    if i + 1 == len(levels):
      return 0
    if _is_decreasing_safely(i, level, levels):
      if direction == Direction.ASCENDING:
        return i + 1
      elif direction == Direction.NOT_SET:
        direction = Direction.DESCENDING
      continue
    elif _is_increasing_safely(i, level, levels) and direction != Direction.DESCENDING:
      if direction == Direction.DESCENDING:
        return i + 1
      elif direction == Direction.NOT_SET:
        direction = Direction.ASCENDING
    else:
      return i + 1
  return 101


def _is_decreasing_safely(i: int, level: int, levels: list[int]) -> bool:
  return level > levels[i + 1] and level - levels[i + 1] <= 3


def _is_increasing_safely(i: int, level: int, levels: list[int]) -> bool:
  return level < levels[i + 1] and levels[i + 1] - level <= 3


def _text_to_reports(text: str) -> list[list[int]]:
  result = []
  for line in text.splitlines():
    line = line.strip()
    if not line:
      continue
    report = [int(num) for num in line.split()]
    result.append(report)
  return result
