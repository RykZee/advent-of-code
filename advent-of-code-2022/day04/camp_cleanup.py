def get_overlapping_sections(sections):
    fully_overlapped = 0
    partially_overlapped = 0

    sections_list = [item for item in sections.splitlines() if item != ""]
    for pair in sections_list:
        worker1, worker2 = pair.split(",")

        w1_start, w1_end = _get_start_end(worker1)
        w2_start, w2_end = _get_start_end(worker2)

        if _is_inbetween(w1_start, w1_end, w2_start, w2_end):
            fully_overlapped += 1
        if _has_any_in_between(w1_start, w1_end, w2_start, w2_end):
            partially_overlapped += 1

    return fully_overlapped, partially_overlapped


def _has_any_in_between(start, end, other_start, other_end):
    if start <= other_start <= end:
        return True
    elif other_start <= start <= other_end:
        return True
    elif start <= other_end <= end:
        return True
    elif other_start <= end <= other_end:
        return True
    return False


def _is_inbetween(start, end, other_start, other_end):
    if other_start >= start and other_end <= end:
        return True
    elif start >= other_start and end <= other_end:
        return True
    return False


def _get_start_end(worker):
    start, end = worker.split("-")
    return int(start), int(end)
