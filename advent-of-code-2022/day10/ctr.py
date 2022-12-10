def get_signal_strength(raw):
    cycle = 1
    x = 1
    signal_strengths = []
    for line in raw.splitlines():
        if _should_check_signal_strength(cycle):
            signal_strengths.append(x * cycle)
        if line == "noop":
            cycle += 1
        if "addx" in line:
            addx = int(line.split(" ")[1])
            cycle += 1
            if _should_check_signal_strength(cycle):
                signal_strengths.append(x * cycle)
            cycle += 1
            x += addx
    return signal_strengths


def get_render_image(raw):
    cycle = 0
    sprite_position = 1
    str_builder = ""
    for line in raw.splitlines():
        if cycle % 40 == 0 and cycle > 0:
            str_builder += "\n"
            cycle = 0
        str_builder += _draw_pixel(cycle, sprite_position)
        if line == "noop":
            cycle += 1
        elif "addx" in line:
            cycle += 1
            if cycle % 40 == 0:
                str_builder += "\n"
                cycle = 0
            str_builder += _draw_pixel(cycle, sprite_position)
            cycle += 1
            addx = int(line.split(" ")[1])
            sprite_position += addx
    return str_builder


def _draw_pixel(cycle, sprite_position):
    return "#" if cycle in range(sprite_position - 1, sprite_position + 2) else "."


def _should_check_signal_strength(cycle):
    return cycle >= 20 and cycle % 40 == 20
