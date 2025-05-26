import re

def calculate_safety_factor(file_path="input.txt"):
    """
    Calculates the robot safety factor based on their positions after 100 seconds.

    This reads the initial positions and velocities from a file, computes their
    final positions in a grid, counts how many robots end up in each quadrant,
    and returns the product of these counts.

    Args:
        file_path (str): The path to the input text file.

    Returns:
        int: The calculated safety factor.
    """

    # Definition of the dimensions and simulation time.
    WIDTH = 101
    HEIGHT = 103
    TIME = 100

    # Determine the center lines of the grid.
    CENTER_X = WIDTH // 2
    CENTER_Y = HEIGHT // 2

    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None

    # Initialize quadrant counts [Top-Left, Top-Right, Bottom-Left, Bottom-Right]
    quadrant_counts = [0, 0, 0, 0]

    for line in lines:
        # Extract all integer values from the line.
        numbers = re.findall(r'-?\d+', line)
        if len(numbers) == 4:
            px, py, vx, vy = map(int, numbers)

            # Calculate the final position with wrapping edges.
            final_x = (px + vx * TIME) % WIDTH
            final_y = (py + vy * TIME) % HEIGHT

            # Skip robots that are on a center line.
            if final_x == CENTER_X or final_y == CENTER_Y:
                continue

            # Determine a robot's quadrant.
            is_left = final_x < CENTER_X
            is_top = final_y < CENTER_Y

            if is_top and is_left:
                quadrant_counts[0] += 1  # Top-Left
            elif is_top and not is_left:
                quadrant_counts[1] += 1  # Top-Right
            elif not is_top and is_left:
                quadrant_counts[2] += 1  # Bottom-Left
            else:  # Not top and not left
                quadrant_counts[3] += 1  # Bottom-Right

    # Calculate the final safety factor by multiplying the counts
    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count
        
    return safety_factor

if __name__ == "__main__":
    safety_factor = calculate_safety_factor()
    if safety_factor is not None:
        print(f"The final safety factor after 100 seconds is: {safety_factor}")