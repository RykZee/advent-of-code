from typing import List, Tuple, Dict, Set


def calculate_safety_manual(text: str) -> int:
    raw_rules, updates = _rules_and_updates(text)
    rules = _sort_according_to_rules(raw_rules)
    return _match_updates(rules, updates)


def _rules_and_updates(text: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    rules = []
    updates = []
    for line in text.splitlines():
        if "|" in line:
            no1, no2 = line.split("|")
            rules.append((int(no1), int(no2)))
        elif "," in line:
            update = [int(number) for number in line.split(",")]
            updates.append(update)

    return rules, updates


def _sort_according_to_rules(raw_rules: List[Tuple[int, int]]) -> Dict[int, Set[int]]:
    rules: Dict[int, Set[int]] = {}
    for first, second in raw_rules:
        if not rules.get(first):
            rules[first] = set()
        rules[first].add(second)
    return rules


def _match_updates(rules: Dict[int, Set[int]], updates: List[List[int]]) -> int:
    result = 0
    for update in updates:
        numbers = set()
        for number in update:
            if rules.get(number, set()).intersection(numbers):
                break
            numbers.add(number)
        if len(numbers) == len(update):
            median = update[len(update) // 2]
            result += median

    return result
