filename = 'input.txt'

def read_file(filename):
    left,right = [],[]
    with open(filename) as file:
        for line in file:
            values = line.split()
            left.append(int(values[0]))
            right.append(int(values[1]))
    left.sort()
    right.sort()
    return left, right

def calculate_total_difference(left,right):
    total_difference = 0  # Local variable
    for i in range(len(left)):
        total_difference += abs(left[i] - right[i])
    return total_difference

# Main logic
left,right = read_file(filename)
total_difference = calculate_total_difference(left,right)
print(f"Total difference: {total_difference}")
