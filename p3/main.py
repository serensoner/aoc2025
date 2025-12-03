from common import test, solve


def mapper(line: str) -> dict[int, list[int]]:
    m = {}
    for p in range(len(line)):
        d = int(line[p])
        if d not in m:
            m[d] = []
        m[d].append(p)

    for k in m.keys():
        m[k] = sorted(m[k])

    return m


def find_largest_digit(mapped: dict, remaining_digits: int, line_len: int, prev_pos: int) -> tuple[int, int]:
    for h in range(9, 0, -1):
        if not mapped.get(h):
            continue
        for pos in mapped.get(h):
            if pos > prev_pos and line_len - pos >= remaining_digits:
                return h, pos

    raise Exception(f"couldnt find {remaining_digits=}, {line_len=}, {mapped=}")


def solver(inp: str, num_digits: int) -> str:
    lines = inp.splitlines()
    sums = 0
    for l in lines:
        digits = []
        mapped = mapper(l)
        line_len = len(l)
        prev_pos = -1
        for digit_ctr in range(num_digits):
            digit, pos = find_largest_digit(mapped, num_digits - digit_ctr, line_len, prev_pos)
            mapped[digit].remove(pos)
            digits.append(digit)
            prev_pos = pos

        sums += int("".join([str(s) for s in digits]))

    return str(sums)


def part1(inp: str) -> str:
    return solver(inp, 2)


def part2(inp: str) -> str:
    return solver(inp, 12)


if __name__ == "__main__":
    if test(part1, "1"):
        solve(part1, "1")
    if test(part2, "2"):
        solve(part2, "2")
