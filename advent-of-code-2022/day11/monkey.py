def do_monkey_business(raw):
    monkeys = _parse_raw_to_monkeys(raw)

    for i in range(20):
        for monkey in monkeys:
            _do_monkey_business(monkey, monkeys)
    inspections = [monkey["inspections"] for monkey in monkeys]
    inspections.sort()
    return inspections[-2] * inspections[-1]


def _do_monkey_business(monkey, monkeys):
    for i, old in enumerate(monkey["items"]):
        new = eval(monkey["operation"])
        new = new // 3
        monkey["items"][i] = new
        if new % monkey["test"] == 0:
            monkeys[monkey["true"]]["items"].append(new)
        else:
            monkeys[monkey["false"]]["items"].append(new)
        monkey["inspections"] += 1
    monkey["items"] = []


def _parse_raw_to_monkeys(raw):
    monkeys = []
    for line in raw.splitlines():
        if "Monkey" in line:
            num = int(line.split(" ")[1][:-1])
            monkey = {
                "items": [],
                "operation": "",
                "test": 0,
                "true": 0,
                "false": 0,
                "inspections": 0,
            }
            monkeys.append(monkey)
        elif "Starting items" in line:
            for item in line.split(":")[1].split(","):
                monkeys[num]["items"].append(int(item.strip()))
        elif "Operation" in line:
            monkeys[num]["operation"] += line.split("= ")[1].strip()
        elif "Test" in line:
            monkeys[num]["test"] = int(line.split(" ")[-1])
        elif "If true" in line:
            monkeys[num]["true"] = int(line.split(" ")[-1])
        elif "If false" in line:
            monkeys[num]["false"] = int(line.split(" ")[-1])
    return monkeys
