from common import test, solve


def mod_calc(num_digits: int, odds: bool = False) -> list[int]:
    if num_digits % 2 == 0:
        if odds:
            return [int("1" * n) for n in range(2, int(num_digits / 2) + 1)]
        else:
            return [10 ** int(num_digits / 2) + 1]
    else:
        return [int("1" * num_digits)]


def invalid_in_range_same_num_digits_(num1: int, num2: int, m: int) -> list[int]:

    parts1 = divmod(num1, m)
    parts2 = divmod(num2, m)
    start = parts1[0] if parts1[1] == 0 else parts1[0] + 1
    end = parts2[0]
    return [el * m for el in range(start, end + 1)]


def invalid_in_range_same_num_digits(num1: int, num2: int, divisors: list[int]) -> list[int]:
    ret = []
    for m in divisors:
        ret += invalid_in_range_same_num_digits_(num1, num2, m)

    return ret


def invalid_in_range(num1: int, num2: int, odds: bool = False) -> list[int]:
    num_digits_1 = len(str(num1))
    num_digits_2 = len(str(num2))

    if num_digits_1 == num_digits_2:
        if num_digits_1 % 2 != 0:
            return []

        divisors = mod_calc(num_digits_1, odds)
        print(f"{divisors=}, {num1=}, {num2=}")
        return invalid_in_range_same_num_digits(num1, num2, divisors)

    else:
        invalids = []
        while True:
            if num_digits_1 > num_digits_2:
                break
            if num_digits_1 %2 == 0 or odds:
                m = mod_calc(num_digits_1, odds)
            else:
                num_digits_1 += 1
                continue

            lowest = max(10 ** (num_digits_1 - 1), num1)
            highest = min(10 ** num_digits_1 - 1, num2)
            invalids += invalid_in_range_same_num_digits(lowest, highest, m)
            num_digits_1 += 1

        return invalids


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
    # if test(part1, "1"):
    #     solve(part1, "1")
    if test(part2, "2"):
        solve(part2, "2")
