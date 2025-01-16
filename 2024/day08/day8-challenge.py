with open("input.txt", "r") as file:
    data = file.read()
data = data.splitlines()
data = [list(i) for i in data]

antenna_positions = {}
for row in range(len(data)):
    for col in range(len(data[0])):
        char = data[row][col]
        if char != ".":
            antenna_positions.setdefault(char, []).append((row, col))

antinodes = set()
bounds = len(data)
for positions in antenna_positions.values():
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                pos1, pos2 = positions[i], positions[j]
                dX = pos2[0] - pos1[0]
                dY = pos2[1] - pos1[1]

                if pos1 not in antinodes:
                    antinodes.add(pos1)
                if pos2 not in antinodes:
                    antinodes.add(pos2)

                if dX == 0:
                    for row in range(bounds):
                        location = (row, pos1[1])
                        if location not in antinodes:
                            antinodes.add(location)

                if dY == 0:
                    for col in range(bounds):
                        location = (pos1[0], col)
                        if location not in antinodes:
                            antinodes.add(location)

                #diagonal
                gcd = abs(dX) + abs(dY)  #MDC
                while gcd > 1:
                    if dX % gcd == 0 and dY % gcd == 0:
                        dX //= gcd
                        dY //= gcd
                    gcd -= 1

                antinode0 = (pos1[0] - dX, pos1[1] - dY)
                while 0 <= antinode0[0] < bounds and 0 <= antinode0[1] < bounds:
                    if antinode0 not in antinodes:
                        antinodes.add(antinode0)
                    antinode0 = (antinode0[0] - dX, antinode0[1] - dY)

                antinode1 = (pos1[0] + dX, pos1[1] + dY)
                while 0 <= antinode1[0] < bounds and 0 <= antinode1[1] < bounds:
                    if antinode1 not in antinodes:
                        antinodes.add(antinode1)
                    antinode1 = (antinode1[0] + dX, antinode1[1] + dY)

print(f"Total Unique Locations: {len(antinodes)}")
#I hated this thank you