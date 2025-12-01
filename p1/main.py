from common import test, solve

def part2(inp: str) -> str:
    passwords = [(l[0], int(l[1:])) for l in inp.splitlines()]
    zeroes = 0
    last_num = 50
    for p in passwords:
        full_turns, num_turns = divmod(p[1], 100)
        zeroes += full_turns
        if p[0] == "L":
            new_num = last_num - num_turns
        else:
            new_num = last_num + num_turns

        if last_num != 0:
            if new_num % 100 == 0 or new_num < 0 or new_num > 100:
                zeroes += 1

        last_num = new_num % 100

    return str(zeroes)

def part1(inp: str) -> str:
    passwords = [(l[0], int(l[1:])) for l in inp.splitlines()]
    zeroes = 0
    last_num = 50
    for p in passwords:
        if p[0] == "L":
            last_num -= p[1]
        else:
            last_num += p[1]

        last_num = last_num % 100
        if last_num == 0:
            zeroes += 1

    return str(zeroes)


if __name__ == "__main__":
    if test(part1, "1"):
        solve(part1, "1")
    if test(part2, "2"):
        solve(part2, "2")
