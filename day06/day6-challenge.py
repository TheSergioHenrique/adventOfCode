#THIS IS THE MOST AGGREGIOUS CODE I'VE EVER WROTE. LOOK AT THIS MESS.
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def simulate_guard_path_with_obstruction(map_lines, obstruction=None):
    grid = [list(line) for line in map_lines]
    rows, cols = len(grid), len(grid[0])

    #(dx, dy) == UP, RIGHT, DOWN & LEFT.
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_symbols = ['^', '>', 'v', '<']

    if obstruction:
        r_obs, c_obs = obstruction
        grid[r_obs][c_obs] = '#'

    #Searching the guard in the input
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_symbols:
                pos = (r, c)
                direction = direction_symbols.index(grid[r][c])
                break

    visited_states = set()  
    while True:
        if (pos, direction) in visited_states:
            return True

        visited_states.add((pos, direction))
        r, c = pos
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            return False  

        if grid[nr][nc] == '#':
            direction = (direction + 1) % 4  # Vira à direita
        else:
            pos = (nr, nc) 

def find_positions_to_create_loop(map_lines):
    print("I'm slow. Wait...")
    rows, cols = len(map_lines), len(map_lines[0])
    valid_positions = []

    for r in range(rows):
        for c in range(cols):
            if map_lines[r][c] in ['#', '^', '>', 'v', '<']:
                continue
            if simulate_guard_path_with_obstruction(map_lines, obstruction=(r, c)):
                valid_positions.append((r, c))

    return valid_positions

input_map = read_input('input.txt')

loop_positions = find_positions_to_create_loop(input_map)

print(f"Done! Total Loopable positions: {len(loop_positions)}")
