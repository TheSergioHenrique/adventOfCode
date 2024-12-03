#REGEX time!!!!
import re
filename = 'input.txt'

def read_file(filename):
    with open('input.txt', 'r') as filename:
        corrupted_data = filename.read()
    return corrupted_data


#Regex to filter only the valid instructions from the input.
regex = r"mul\((\d+),(\d+)\)"

corrupted_data = read_file(filename)

matches = re.findall(regex, corrupted_data)

total = sum(int(a) * int(b) for a, b in matches)

print(f"The total value is: {total}")
