from typing import List
from dataclasses import dataclass

Finished = object()


@dataclass(frozen=True)
class Position:
    x: int
    y: int
    direction: str


def guard_path(text: str) -> int:
    grid = _get_grid(text)
    return _get_path_visited(grid)


def _get_grid(text: str) -> List[List[str]]:
    path = []
    for line in text.splitlines():
        path.append(list(line))
    return path


def _get_path_visited(grid: List[List[str]]) -> int:
    position: Position = _get_position(grid)

    while True:
        update = _move(position, grid)
        if update == Finished:
            return _result(grid)
        position = update  # type: ignore
        # _print(grid)


def _move(position: Position, grid: List[List[str]]) -> Position | object:
    match position.direction:
        case "<":
            return _move_left(position, grid)
        case "v":
            return _move_down(position, grid)
        case "^":
            return _move_up(position, grid)
        case ">":
            return _move_right(position, grid)


def _move_left(position: Position, grid: List[List[str]]) -> Position | object:
    if position.x - 1 < 0:
        grid[position.y][position.x] = "X"
        return Finished
    elif grid[position.y][position.x - 1] == "#":
        grid[position.y][position.x] = "^"
        return Position(x=position.x, y=position.y, direction="^")

    new_position = Position(
        x=position.x - 1, y=position.y, direction=position.direction
    )
    grid[position.y][position.x] = "X"
    grid[new_position.y][new_position.x] = new_position.direction
    return new_position


def _move_down(position: Position, grid: List[List[str]]) -> Position | object:
    if position.y + 1 >= len(grid):
        grid[position.y][position.x] = "X"
        return Finished
    elif grid[position.y + 1][position.x] == "#":
        grid[position.y][position.x] = "<"
        return Position(x=position.x, y=position.y, direction="<")

    new_position = Position(
        x=position.x, y=position.y + 1, direction=position.direction
    )
    grid[position.y][position.x] = "X"
    grid[new_position.y][new_position.x] = new_position.direction
    return new_position


def _move_up(position: Position, grid: List[List[str]]) -> Position | object:
    if position.y - 1 < 0:
        grid[position.y][position.x] = "X"
        return Finished
    elif grid[position.y - 1][position.x] == "#":
        grid[position.y][position.x] = ">"
        return Position(x=position.x, y=position.y, direction=">")

    new_position = Position(
        x=position.x, y=position.y - 1, direction=position.direction
    )
    grid[position.y][position.x] = "X"
    grid[new_position.y][new_position.x] = new_position.direction
    return new_position


def _move_right(position: Position, grid: List[List[str]]) -> Position | object:
    if position.x + 1 > len(grid[position.y]):
        grid[position.y][position.x] = "X"
        return Finished
    elif grid[position.y][position.x + 1] == "#":
        grid[position.y][position.x] = "v"
        return Position(x=position.x, y=position.y, direction="v")

    new_position = Position(
        x=position.x + 1, y=position.y, direction=position.direction
    )
    grid[position.y][position.x] = "X"
    grid[new_position.y][new_position.x] = new_position.direction
    return new_position


def _print(grid: List[List[str]]) -> None:
    print("-----------------------------------------------------")
    for row in grid:
        print(row)
    print("-----------------------------------------------------")


def _result(grid: List[List[str]]) -> int:
    result = 0
    for row in grid:
        for col in row:
            if col == "X":
                result += 1
    return result

def _get_position(grid: List[List[str]]) -> Position:
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col in ["<", "v", "^", ">"]:
                return Position(x=x, y=y, direction=col)
    raise RuntimeError("No position found, something is wrong")
