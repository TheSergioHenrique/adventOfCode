#REGEX time!!!!
import re
filename = 'input.txt'

def read_file(filename):
    with open('input.txt', 'r') as filename:
        corrupted_data = filename.read()
    return corrupted_data

#Regex to filter only the valid instructions from the input.
regex = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"

corrupted_data = read_file(filename)
mul_state=True
total=0

filtered_data = re.findall(regex, corrupted_data)

for instruction, a, b in filtered_data:
    if instruction == "do()":
        mul_state = True
    elif instruction == "don't()":
        mul_state = False
    elif "mul" in instruction and mul_state:
        total += int(a) * int(b)

print(f"The total value is: {total}")
