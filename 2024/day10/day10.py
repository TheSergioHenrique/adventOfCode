from collections import deque

def read_height_map(path):
    """
    Reads the input file and returns a 2D list of integers.
    """
    with open(path) as f:
        return [list(map(int, line.strip())) for line in f if line.strip()]

def find_trailheads(grid):
    """
    Returns a list of (r,c) positions where grid[r][c] == 0.
    """
    heads = []
    for r, row in enumerate(grid):
        for c, h in enumerate(row):
            if h == 0:
                heads.append((r, c))
    return heads

def score_from_head(grid, start):
    """
    Breadth-First Search. Thanks, Data Structures lessons. 
    """
    R, C = len(grid), len(grid[0])
    sr, sc = start
    visited = set([(sr, sc)])
    q = deque([(sr, sc)])
    reached_nines = set()
    while q:
        r, c = q.popleft()
        h = grid[r][c]
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                nh = grid[nr][nc]
                # only step if it’s exactly one higher
                if nh == h + 1:
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    if nh == 9:
                        reached_nines.add((nr, nc))
    return len(reached_nines)

def main():
    grid = read_height_map('input.txt')
    heads = find_trailheads(grid)
    total_score = sum(score_from_head(grid, h) for h in heads)
    print("Sum of all trailhead scores =", total_score)

if __name__ == "__main__":
    main()
