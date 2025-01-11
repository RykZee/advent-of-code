def safe_reports(text: str) -> int:
    reports = _text_to_reports(text)

    result = 0
    for report in reports:
        if is_safe(report):
            result += 1
    return result


def is_safe(report: list[int]) -> bool:
    order = _ascending_or_descending(report)
    match order:
        case "ASCENDING":
            return _check_ascending(report)
        case "DESCENDING":
            return _check_descending(report)


def _check_ascending(report: list[int]) -> bool:
    for i, current_level in enumerate(report):
        if i == 0:
            continue
        if current_level < report[i - 1]:
            return False
        difference = current_level - report[i - 1]
        if not 1 <= difference <= 3:
            return False
    return True


def _check_descending(report: list[int]) -> bool:
    for i, current_level in enumerate(report):
        if i == 0:
            continue
        if current_level > report[i - 1]:
            return False
        difference = report[i - 1] - current_level
        if not 1 <= difference <= 3:
            return False
    return True


def _ascending_or_descending(report: list[int]) -> str:
    return "ASCENDING" if report[0] < report[1] else "DESCENDING"


def _text_to_reports(text: str) -> list[list[int]]:
    result = []
    for line in text.split("\n"):
        report = [int(num) for num in line.split()]
        result.append(report)
    return result
