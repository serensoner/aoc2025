import math

from common import test, solve


def part2(inp: str) -> str:
    lines = inp.splitlines()
    start_char = 0
    total = 0
    max_line_len = max(len(l) for l in lines)
    while True:
        op = lines[-1][start_char]
        next_ops = [idx for idx, c in enumerate(lines[-1][start_char+1:]) if c != " "]
        if not next_ops:
            next_start_char = max_line_len
        else:
            next_start_char = next_ops[0] + start_char 
        digits = []
        for c in range(start_char, next_start_char):
            chars = [l[c] for l in lines[:-1] if c < len(l) and l[c] != " " ]
            digits.append(int(''.join(chars)))
        
        print(digits, op)
        if op == "*":
            total += math.prod(digits)
        elif op == "+":
            total += sum(digits)

        start_char = next_start_char + 1
        if not next_ops:
            break

    return str(total)


def part1(inp: str) -> str:
    lines = inp.splitlines()
    ops = [s.strip() for s in lines[-1].split(" ") if s.strip()]
    nums = [[int(s.strip()) for s in l.split(" ") if s] for l in lines[:-1]]
    total = 0
    for idx, op in enumerate(ops):
        nums_ = [n[idx] for n in nums]
        if op == "*":
            total += math.prod(nums_)
        elif op == "+":
            total += sum(nums_)
    return str(total)


if __name__ == "__main__":
    if test(part1, "1"):
        solve(part1, "1")
    if test(part2, "2"):
        solve(part2, "2")
