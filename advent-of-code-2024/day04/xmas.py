def find_xmas_hits(text: str) -> int:
    grid = _grid_matrix(text)
    _print_grid(grid)

    return _xmas_occurrances(grid)


def find_x_mas_hits(text: str) -> int:
    grid = _grid_matrix(text)
    return _x_mas_occurrances(grid)


def _grid_matrix(text: str) -> list[list[str]]:
    grid = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        grid.append(list(line))
    return grid


def _xmas_occurrances(grid: list[list[str]]) -> int:
    result = 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if _has_xmas(grid, x, y):
                result += 1
            if _has_reverse_xmas(grid, x, y):
                result += 1
            if _has_vertical_xmas(grid, x, y):
                result += 1
            if _has_reverse_vertical_xmas(grid, x, y):
                result += 1
            if _has_north_east_xmas(grid, x, y):
                result += 1
            if _has_south_east_xmas(grid, x, y):
                result += 1
            if _has_south_west_xmas(grid, x, y):
                result += 1
            if _has_north_west_xmas(grid, x, y):
                result += 1
    return result


def _x_mas_occurrances(grid: list[list[str]]) -> int:
    result = 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if _has_x_mas(grid, x, y):
                result += 1
    return result


def _has_x_mas(grid: list[list[str]], x: int, y: int) -> bool:
    if y + 2 >= len(grid) or x + 2 >= len(grid[y]):
        return False
    target1 = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] in ["MAS", "SAM"]
    target2 = grid[y][x + 2] + grid[y + 1][x + 1] + grid[y + 2][x] in ["MAS", "SAM"]
    return target1 and target2


def _has_xmas(grid: list[list[str]], x: int, y: int) -> bool:
    target = grid[y][x : x + 4]
    return "".join(target) == "XMAS"


def _has_reverse_xmas(grid: list[list[str]], x: int, y: int) -> bool:
    target = grid[y][x - 3 : x + 1]
    return "".join(target) == "XMAS"[::-1]


def _has_vertical_xmas(grid: list[list[str]], x: int, y: int) -> bool:
    if y + 3 >= len(grid):
        return False
    target = grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x]
    return target == "XMAS"


def _has_reverse_vertical_xmas(grid: list[list[str]], x: int, y: int) -> bool:
    if y - 3 < 0:
        return False
    target = grid[y][x] + grid[y - 1][x] + grid[y - 2][x] + grid[y - 3][x]
    return target == "XMAS"


def _has_north_east_xmas(grid: list[list[str]], x: int, y: int) -> bool:
    if y - 3 < 0 or x + 3 >= len(grid[y]):
        return False
    target = grid[y][x] + grid[y - 1][x + 1] + grid[y - 2][x + 2] + grid[y - 3][x + 3]
    return target == "XMAS"


def _has_south_east_xmas(grid: list[list[str]], x: int, y: int) -> bool:
    if y + 3 >= len(grid) or x + 3 >= len(grid[y]):
        return False
    target = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] + grid[y + 3][x + 3]
    return target == "XMAS"


def _has_south_west_xmas(grid: list[list[str]], x: int, y: int) -> bool:
    if y + 3 >= len(grid) or x - 3 < 0:
        return False
    target = grid[y][x] + grid[y + 1][x - 1] + grid[y + 2][x - 2] + grid[y + 3][x - 3]
    return target == "XMAS"


def _has_north_west_xmas(grid: list[list[str]], x: int, y: int) -> bool:
    if y - 3 < 0 or x - 3 < 0:
        return False
    target = grid[y][x] + grid[y - 1][x - 1] + grid[y - 2][x - 2] + grid[y - 3][x - 3]
    return target == "XMAS"


def _print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print(row)
