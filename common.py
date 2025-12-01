from typing import Callable


def test(func: Callable, part: str) -> bool:
    with open(f"sample{part}.txt") as f:
        inp = f.read()

    output = func(inp)

    with open(f"output{part}.txt") as f:
        sample_output = f.read()

    print(f"{output=}, {sample_output=}")

    return str(output) == str(sample_output)


def solve(func: Callable, part: str) -> None:
    with open(f"input.txt") as f:
        inp = f.read()

    output = func(inp)

    print(f"{output=}")
    return output
