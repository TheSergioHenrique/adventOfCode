def parse_disk_map(disk_map):
    """
    Convert the dense disk map string into a list of blocks:
    - Digits at even positions (0, 2, 4, …) are file lengths.
    - Digits at odd positions (1, 3, 5, …) are free-space lengths.
    Each file block gets an identifier (0, 1, 2, …) in the order encountered.
    Free-space blocks become '.'.
    """
    i = 0
    blocks = []
    file_id = 0
    while i < len(disk_map):
        # read file length and create that many file_id blocks
        file_len = int(disk_map[i])
        i += 1
        blocks.extend([str(file_id)] * file_len)
        file_id += 1
        # read free-space length (if any) and create that many '.'
        if i < len(disk_map):
            space_len = int(disk_map[i])
            i += 1
            blocks.extend(['.'] * space_len)
    return blocks

def compact_files(blocks):
    """
    Move each file (as a whole) at most once, in decreasing file ID order:
      1. For file_id = max,…,0:
      2. Find its current span (start index).
      3. Find the leftmost contiguous '.' run to the left of that span
         whose length is >= the file's length.
      4. If found, copy the file_id into that span and replace the original
         span with '.'.
    """
    blocks = blocks.copy()
    # determine how many files there are
    max_id = max(int(v) for v in blocks if v != '.')
    for fid in range(max_id, -1, -1):
        # find current span of this file_id
        positions = [i for i,v in enumerate(blocks) if v == str(fid)]
        if not positions:
            continue
        length = len(positions)
        start = positions[0]
        # scan for runs of '.' that end before start
        best = None
        run_len = 0
        run_start = None
        for i, v in enumerate(blocks[:start]):
            if v == '.':
                if run_start is None:
                    run_start = i
                run_len += 1
            else:
                if run_len >= length:
                    best = run_start
                    break
                run_start = None
                run_len = 0
        # final check at boundary
        if best is None and run_len >= length:
            best = run_start
        # if we found a fit, move the file
        if best is not None:
            # clear original span
            for i in positions:
                blocks[i] = '.'
            # fill new span
            for j in range(best, best + length):
                blocks[j] = str(fid)
    return blocks

def calculate_checksum(blocks):
    """
    Compute checksum by summing (position * file_id) for each file block.
    Skip '.' blocks.
    """
    checksum = 0
    for pos, val in enumerate(blocks):
        if val != '.':
            checksum += pos * int(val)
    return checksum

def main():
    # read the single input line from the file
    with open('input.txt', 'r') as f:
        line = f.readline().strip()
    # build blocks, compact by whole-file moves, and compute checksum
    blocks = parse_disk_map(line)
    compacted = compact_files(blocks)
    print("Checksum:", calculate_checksum(compacted))

if __name__ == "__main__":
    main()
