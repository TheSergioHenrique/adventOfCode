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
            if i != j:  #Checking to see if they are the same
                pos1 = positions[i]
                pos2 = positions[j]

                delta_row = pos2[0] - pos1[0]
                delta_col = pos2[1] - pos1[1]

                antinode1 = (pos1[0] - delta_row, pos1[1] - delta_col)
                if 0 <= antinode1[0] < bounds and 0 <= antinode1[1] < bounds:
                    antinodes.add(antinode1)

                antinode2 = (pos2[0] + delta_row, pos2[1] + delta_col)
                if 0 <= antinode2[0] < bounds and 0 <= antinode2[1] < bounds:
                    antinodes.add(antinode2)

print(f"Total Unique Locations: {len(antinodes)}")
