from typing import Union

from common import test, solve


def part1(inp: str) -> str:
    tp_rolls = create_adjacent_matrix(inp.splitlines())
    accessible = []
    for current, adjacent_tp_rolls in tp_rolls.items():
        if len(adjacent_tp_rolls) < 4:
            accessible.append(current)
            tp_rolls[current] = []

    return str(len(accessible))


def create_adjacent_matrix(lines: list[str]) -> dict[tuple[int, int], Union[bool, list[tuple[int, int]]]]:
    tp_rolls = {}
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "@":
                tp_rolls[(x, y)] = []
                adjacent_list = [
                    (x + i, y + j)
                    for i in range(-1, 2) for j in range(-1, 2)
                    if not (i == 0 and j == 0)
                ]
                for adj in adjacent_list:
                    if adj in tp_rolls:
                        tp_rolls[(x, y)].append(adj)
                        tp_rolls[adj].append((x, y))

    return tp_rolls


def part2(inp: str) -> str:
    tp_rolls = create_adjacent_matrix(inp.splitlines())

    accessible = []
    while True:
        has_changed = False
        for curr, adjacent_tp_rolls in tp_rolls.items():
            if adjacent_tp_rolls is not False and len(adjacent_tp_rolls) < 4:
                for adj in adjacent_tp_rolls:
                    tp_rolls[adj].remove(curr)
                accessible.append(curr)
                has_changed = True
                tp_rolls[curr] = False
        if not has_changed:
            break

    return str(len(accessible))


if __name__ == "__main__":
    if test(part1, "1"):
        solve(part1, "1")
    if test(part2, "2"):
        solve(part2, "2")
