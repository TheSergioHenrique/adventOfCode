def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def simulate_guard_path(map_lines):
    grid = [list(line) for line in map_lines]
    rows, cols = len(grid), len(grid[0])

    #(dx, dy) == UP, RIGHT, DOWN & LEFT.
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_symbols = ['^', '>', 'v', '<']

    #Searching the guard in the input
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_symbols:
                pos = (r, c)
                direction = direction_symbols.index(grid[r][c])
                break

    visited = set()
    visited.add(pos)
    while True:
        r, c = pos
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            break

        #dealing with #
        if grid[nr][nc] == '#':
            direction = (direction + 1) % 4
        else:
            pos = (nr, nc)
            visited.add(pos)

    for r, c in visited:
        grid[r][c] = 'X'

    visited_count = len(visited)
    return [''.join(row) for row in grid], visited_count


input_map = read_input('input.txt')
output_map, visited_count = simulate_guard_path(input_map)

print("Visualizing the map:")
for line in output_map:
    print(line)

#actual answer lol
print(f"\n Visited positions: {visited_count}")
