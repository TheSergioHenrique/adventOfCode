def read_grid(input):
    with open(input, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    x_mas_count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                mas1 = sam1 = mas2 = sam2 = False

                if (is_valid(i - 1, j - 1) and is_valid(i + 1, j + 1)):
                    mas1 = (
                        grid[i - 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S'
                    )
                    sam1 = (
                        grid[i - 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M'
                    )

                if (is_valid(i - 1, j + 1) and is_valid(i + 1, j - 1)):
                    mas2 = (
                        grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S'
                    )
                    sam2 = (
                        grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M'
                    )

                if (mas1 or sam1) and (mas2 or sam2):
                    x_mas_count += 1

    return x_mas_count


if __name__ == "__main__":
    grid = read_grid('input.txt')
    result = count_x_mas(grid)
    print(f"Total occurrences of X-MAS: {result}")