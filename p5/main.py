from common import test, solve


def read_sort_input(inp: str) -> tuple[list[tuple[int, int]], list[str]]:
    lines = inp.splitlines()
    id_lno = None
    ranges = []
    ids = []
    for lno, l in enumerate(lines):
        if l.strip() == "":
            id_lno = lno + 1
            break
        parts = l.split("-")
        ranges.append((int(parts[0]), int(parts[1])))

    ranges = sorted(ranges, key=lambda x: (x[0], x[1]))
    return ranges, lines[id_lno + 1:]



def part2(inp: str) -> str:
    ranges, _ = read_sort_input(inp)
    last_range: tuple[int, int] = ranges[0]
    current_sum = 0
    for r in ranges[1:]:
        if not last_range or last_range[1] < r[0]:
            current_sum += last_range[1] - last_range[0] + 1
            last_range = r

        else:
            last_range = (last_range[0], max(last_range[1], r[1]))

    current_sum += last_range[1] - last_range[0] + 1
    return str(current_sum)


def is_fresh(num: int, ranges: list[tuple[int, int]]):
    for r in ranges:
        if r[0] > num:
            return False
        if r[0] <= num <= r[1]:
            return True


def part1(inp: str) -> str:
    ranges, id_lines = read_sort_input(inp)

    valid_ctr = 0
    for l in id_lines:
        if is_fresh(int(l), ranges):
            valid_ctr += 1

    return str(valid_ctr)


if __name__ == "__main__":
    if test(part1, "1"):
        solve(part1, "1")
    if test(part2, "2"):
        solve(part2, "2")
