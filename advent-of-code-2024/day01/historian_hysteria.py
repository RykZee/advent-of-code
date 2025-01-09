def find_differences(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()

    result = 0
    for i, first in enumerate(left):
        difference = abs(first - right[i])
        result += difference
    return result


def find_similarities(left: list[int], right: list[int]) -> int:
    occurances_list = [0 for _ in range(max(left) + 1)]

    result = 0
    for number in left:
        if occurances_list[number] == 0:
            occurances = _find_occurances(number, right)
            occurances_list[number] = occurances
        result += number * occurances_list[number]
    return result


def _find_occurances(target: int, right: list[int]) -> int:
    result = 0
    for number in right:
        if number == target:
            result += 1
    return result
