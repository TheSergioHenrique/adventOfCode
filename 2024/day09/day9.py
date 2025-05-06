def parse_disk_map(disk_map):
    """
    Convert the dense disk map string into a list of blocks:
    - Digits at even positions (0, 2, 4, ...) are file lengths.
    - Digits at odd positions (1, 3, 5, ...) are free-space lengths.
    Each file block gets an identifier (0, 1, 2, …) in the order encountered.
    Free space blocks become '.'.
    """
    i = 0
    blocks = []
    file_id = 0
    while i < len(disk_map):
        # Read file length and create file blocks.
        file_len = int(disk_map[i])
        i += 1
        blocks.extend([str(file_id)] * file_len)
        file_id += 1

        # Read free-space length (if present) and create '.' blocks.
        if i < len(disk_map):
            space_len = int(disk_map[i])
            i += 1
            blocks.extend(['.'] * space_len)
    return blocks

def compact_blocks(blocks):
    """
    In each iteration:
      1. Find the first free-space block (leftmost '.').
      2. Find the last file block (rightmost non-'.').
      3. If that file block is to the right of the free space, "teleport" it there.
      4. Repeat until no free space remains to the left of any file block.
    """
    blocks = blocks.copy()
    while True:
        # Position of the first '.'
        try:
            j = blocks.index('.')
        except ValueError:
            # No free-space blocks remain.
            break
        # Position of the rightmost file block.
        i = max(k for k, v in enumerate(blocks) if v != '.')
        # If that block is already left of the free space, we're done.
        if i < j:
            break
        # Move the file block from i to j.
        blocks[j], blocks[i] = blocks[i], '.'
    return blocks

def calculate_checksum(blocks):
    """
    Compute the checksum by summing (position * file_id) for each file block.
    Skip '.' blocks.
    """
    checksum = 0
    for pos, val in enumerate(blocks):
        if val != '.':
            checksum += pos * int(val)
    return checksum

def main():
    # Read the input line from the file.
    with open('input.txt', 'r') as f:
        line = f.readline().strip()
    # Build blocks, compact them, and compute the checksum.
    blocks = parse_disk_map(line)
    compacted = compact_blocks(blocks)
    checksum = calculate_checksum(compacted)
    print("Checksum:", checksum)

if __name__ == "__main__":
    main()
