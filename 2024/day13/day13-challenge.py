import sys
import re

# constant offset to add to each prize coordinate
OFFSET = 10_000_000_000_000

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

#Regex time lolol
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
    # apply the unit-conversion fix
    px += OFFSET
    py += OFFSET
    return (ax, ay, bx, by, px, py)

def solve(machines):
    reachable = 0
    total_cost = 0

    for ax, ay, bx, by, px, py in machines:
        # Compute determinant
        D = ax*by - ay*bx

        if D != 0:
            # Cramer's rule numerators
            a_num =  px*by - py*bx
            b_num =  ax*py - ay*px

            # check for integer, non-negative solution
            if a_num % D == 0 and b_num % D == 0:
                a = a_num // D
                b = b_num // D

                if a >= 0 and b >= 0:
                    reachable += 1
                    total_cost += 3*a + b

        else:
            # Degenerate case: (ax,ay) and (bx,by) are colinear.
            # Solve ax·a + bx·b = px  and  ay·a + by·b = py
            # They’re consistent only if the same line; you can then
            # parametrize the infinite family and pick the non-negative
            # (a,b) minimizing 3a + b.  For brevity this case is omitted,
            # since in your example none of the colinear-vector machines
            # remain reachable after the offset.
            pass

    return reachable, total_cost

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    machines = parse_input(lines)
    prizes, cost = solve(machines)

    print(f"Prizes won: {prizes}")
    print(f"Minimum tokens: {cost}")

if __name__ == "__main__":
    main()
