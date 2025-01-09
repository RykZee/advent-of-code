def find_differences(left: list[int], right: list[int]):
    left.sort()
    right.sort()

    result = 0
    for i, first in enumerate(left):
      difference = abs(first - right[i])
      result += difference
    return result
