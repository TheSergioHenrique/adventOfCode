import sys
import re

def parse_input(lines):
    machines = []
    block = []
    for line in lines:
        line = line.strip()
        if line == "":
            if block:
                machines.append(parse_block(block))
                block = []
        else:
            block.append(line)
    if block:
        machines.append(parse_block(block))
    return machines


def parse_block(block):
    ax = ay = bx = by = px = py = None
    for line in block:
        if line.startswith("Button A"):
            m = re.match(r"Button A: X\+(-?\d+), Y\+(-?\d+)", line)
            ax, ay = map(int, m.groups())
        elif line.startswith("Button B"):
            m = re.match(r"Button B: X\+(-?\d+), Y\+(-?\d+)", line)
            bx, by = map(int, m.groups())
        elif line.startswith("Prize"):
            m = re.match(r"Prize: X=(-?\d+), Y=(-?\d+)", line)
            px, py = map(int, m.groups())
    return (ax, ay, bx, by, px, py)


def solve(machines, max_presses=100):
    total_prizes = 0
    total_cost = 0
    for idx, (ax, ay, bx, by, px, py) in enumerate(machines, start=1):
        best = None  # minimal cost
        for a in range(max_presses+1):
            # Optional early prune: if a*ax > px or a*ay > py: continue
            for b in range(max_presses+1):
                if a*ax + b*bx == px and a*ay + b*by == py:
                    cost = 3*a + b
                    if best is None or cost < best:
                        best = cost
        if best is not None:
            total_prizes += 1
            total_cost += best
    return total_prizes, total_cost

def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    machines = parse_input(lines)
    prizes, cost = solve(machines)
    print(f"Prizes won: {prizes}")
    print(f"Minimum tokens: {cost}")

if __name__ == "__main__":
    main()
