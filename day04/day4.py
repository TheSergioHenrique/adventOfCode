def read_grid(input):
    with open(input, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def search_word_in_grid(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)

    directions = [
        (1, 0),  # UP
        (-1, 0), # DOWN
        (0, -1), # LEFT
        (0, 1),  # RIGHT
        (1, 1),  # UP-RIGHT
        (1, -1), # UP-LEFT
        (-1, 1), # DOWN-RIGHT
        (-1, -1),# DOWN-LEFT
    ]

    count = 0

    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols

    for row in range(rows):
        for col in range(cols):
            for eixoX, eixoY in directions:
                found = True
                for i in range(word_length):
                    new_row, new_col = row + i * eixoX, col + i * eixoY
                    if not is_valid_position(new_row, new_col) or grid[new_row][new_col] != word[i]:
                        found = False
                        break
                if found:
                    count += 1

    return count

def count_xmas_occurrences(grid):
    return search_word_in_grid(grid, "XMAS")

if __name__ == "__main__":
    grid = read_grid("input.txt")
    xmas_count = count_xmas_occurrences(grid)
    print(f"The word 'XMAS' appears {xmas_count} times.")
