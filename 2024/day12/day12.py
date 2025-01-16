from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def is_valid(x, y, grid):
    #Checks if a given cell (x, y) is within the grid boundaries.
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols

def get_region(grid, start_x, start_y, plant_type, visited):
    #Identifies a region and calculates its area and perimeter.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    region_cells = []
    perimeter = 0

    while queue:
        x, y = queue.popleft()
        region_cells.append((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid):
                if grid[nx][ny] == plant_type and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif grid[nx][ny] != plant_type:
                    perimeter += 1
            else:
                perimeter += 1

    area = len(region_cells)
    return area, perimeter

def calculate_total_price(input_map):
    grid = input_map
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0

    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                plant_type = grid[x][y]
                area, perimeter = get_region(grid, x, y, plant_type, visited)
                price = area * perimeter
                total_price += price

    return total_price

if __name__ == "__main__":
    input_file = "input.txt"
    input_map = read_input(input_file)
    total_price = calculate_total_price(input_map)
    print(total_price)
