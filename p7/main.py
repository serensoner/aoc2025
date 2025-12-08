import math

from common import test, solve


def part2(inp: str) -> str:
    lines = inp.splitlines()
    beam_positions = {lines[0].index("S")}
    beams_through = {lines[0].index("S"): 1}
    
    for line in lines[1:]:
        new_beam_positions = set()
        new_beams_through = {}
        
        for idx in beam_positions:
            count = beams_through.get(idx, 0)
            if line[idx] == "^":
                new_beam_positions.update([idx - 1, idx + 1])
                new_beams_through[idx - 1] = new_beams_through.get(idx - 1, 0) + count
                new_beams_through[idx + 1] = new_beams_through.get(idx + 1, 0) + count
            else:
                new_beam_positions.add(idx)
                new_beams_through[idx] = new_beams_through.get(idx, 0) + count
        
        beam_positions = new_beam_positions
        beams_through = new_beams_through

    return str(sum(beams_through.values()))


def part1(inp: str) -> str:
    lines = inp.splitlines()
    beam_positions = set([idx for idx, l in enumerate(lines[0]) if l == "S"])
    split_count = 0
    for l in range(1, len(lines)):
        new_beam_positions = set()
        for idx, c in enumerate(lines[l]):
            if idx in beam_positions:
                if c == "^":
                    if idx - 1 not in new_beam_positions or idx + 1 not in new_beam_positions:
                        split_count += 1
                    new_beam_positions.add(idx - 1)
                    new_beam_positions.add(idx + 1)
                else:
                    new_beam_positions.add(idx)
    
        beam_positions = new_beam_positions

    return str(split_count)

if __name__ == "__main__":
    # if test(part1, "1"):
        # solve(part1, "1")
    if test(part2, "2"):
        solve(part2, "2")
