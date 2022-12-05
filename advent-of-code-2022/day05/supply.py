from itertools import takewhile


def supply_stacks(raw_stack, moves, one_at_a_time=True):
    stack = _get_stack_list_of_lists(raw_stack)
    for line in [item[5:] for item in moves.splitlines() if item != ""]:
        items = line.split(" ")
        move_num = int(items[0])
        from_stack = int(items[2]) - 1
        to_stack = int(items[-1]) - 1
        if one_at_a_time:
            _move_one_box_at_a_time(move_num, to_stack, from_stack, stack)
        else:
            _several_at_a_time(move_num, to_stack, from_stack, stack)

    res = ""
    for nested in stack:
        res += nested[-1]
    return res


def _get_stack_list_of_lists(raw_stack):
    result = []
    cols = int(raw_stack.splitlines()[-1][-1])
    for i in range(cols):
        result.append(list())

    for line in [item for item in raw_stack.splitlines() if item != ""]:
        boxes = line.split()
        if len(max(boxes)) == 1:
            break
        index = 0
        new_line = line
        for box in boxes:
            index = index + int(sum(0.25 for _ in takewhile(str.isspace, new_line)))
            result[index].insert(0, box[1])
            index += 1
            new_line = new_line.strip()[3:]
    return result


def _move_one_box_at_a_time(move_num, to_stack, from_stack, stack):
    for i in range(move_num):
        stack[to_stack].append(stack[from_stack][-1])
        del stack[from_stack][-1]


def _several_at_a_time(move_num, to_stack, from_stack, stack):
    temp = []
    for i in range(move_num, 0, -1):
        temp.append(stack[from_stack][-i])
        del stack[from_stack][-i]
    stack[to_stack].extend(temp)
