from common import test, solve


divisors = {}


def get_mod(num: int) -> int:
    length = len(str(num))
    if divisors.get(length) is not None:
        return divisors.get(length)

    mods = [
        int((10 ** length - 1) / (10 ** k - 1))
        for k in range(1, length)
        if length % k == 0 and int(length / k) >= 2
    ]

    print(f"{length=}, {mods=}")
    divisors[length] = mods
    return mods


def is_divisible_by_mods(num: int) -> bool:
    mods = get_mod(num)
    for mod in mods:
        if num % mod == 0:
            return True

    return False

def part2(inp: str) -> str:
    ranges = [a.split("-") for a in inp.split(",")]
    ranges = [(int(r[0]), int(r[1])) for r in ranges]
    result = 0
    for range_start, range_end in ranges:
        for number in range(range_start, range_end + 1):
            if is_divisible_by_mods(number):
                result += number
    return result


def part1(inp: str) -> str:
    ranges = [a.split("-") for a in inp.split(",")]
    ranges = [(int(r[0]), int(r[1])) for r in ranges]
    invalid_numbers = []
    for r in ranges:
        range_ = invalid_in_range(r[0], r[1])
        print(r, range_)
        invalid_numbers += range_
    return str(sum(invalid_numbers))



def part2(inp: str) -> str:
    ranges = [a.split("-") for a in inp.split(",")]
    ranges = [(int(r[0]), int(r[1])) for r in ranges]
    invalid_numbers = []
    for r in ranges:
        range_ = invalid_in_range(r[0], r[1], odds=True)
        print(r, range_)
        invalid_numbers += range_
    return str(sum(invalid_numbers))


if __name__ == "__main__":
    if test(part1, "1"):
        solve(part1, "1")
    if test(part2, "2"):
        solve(part2, "2")
