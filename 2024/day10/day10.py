from collections import deque, defaultdict

def read_map(path):
    # Read the input file and convert each line into a list of integers
    with open(path) as f:
        return [list(map(int, line.strip())) for line in f if line.strip()]

def find_trailheads(grid):
    # Trailheads are positions with height 0
    return [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0]

def count_paths_from(trail_map, start):
    rows, cols = len(trail_map), len(trail_map[0])
    sr, sc = start

    # Tracks how many distinct paths reach each cell
    path_counts = defaultdict(int)
    path_counts[(sr, sc)] = 1

    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        h = trail_map[r][c]

        # Explore neighbors that are exactly one level higher
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                nh = trail_map[nr][nc]
                if nh == h + 1:
                    if (nr, nc) not in path_counts:
                        q.append((nr, nc))
                    path_counts[(nr, nc)] += path_counts[(r, c)]

    # Sum paths that reach any cell with height 9
    return sum(v for (r, c), v in path_counts.items() if trail_map[r][c] == 9)

def main():
    trail_map = read_map('input.txt')
    trailheads = find_trailheads(trail_map)

    # For each trailhead, count how many unique paths reach height-9 cells
    total_rating = sum(count_paths_from(trail_map, head) for head in trailheads)

    print(f"Sum of all trailhead ratings = {total_rating}")

if __name__ == "__main__":
    main()
