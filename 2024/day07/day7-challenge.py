FILE_PATH = "input.txt"

def read_input(file_path):
    with open(file_path, "r") as file:
        raw_data = file.read().strip().split("\n")
    return [
        (int(target), list(map(int, numbers.split())))
        for target, numbers in (line.split(":") for line in raw_data)
    ]

def generate_combinations(operators, length):
    if length == 0:
        return [""]
    smaller_combinations = generate_combinations(operators, length - 1)
    result = []
    for combination in smaller_combinations:
        for op in operators:
            result.append(combination + op)
    return result

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for number, operator in zip(numbers[1:], operators):
        if operator == "+":
            result += number
        elif operator == "*":
            result *= number
        elif operator == "|":
            result = int(f"{result}{number}")
    return result

def target_reachable(target, numbers, operators):
    combinations = generate_combinations(operators, len(numbers) - 1)
    for operator_combination in combinations:
        if evaluate_expression(numbers, operator_combination) == target:
            return True
    return False

def sum_reachable_targets(equations, operators):
    return sum(
        target
        for target, numbers in equations
        if target_reachable(target, numbers, operators)
    )

def main():
    equations = read_input(FILE_PATH)

    operators = "+*|"
    result = sum_reachable_targets(equations, operators)
    print(f"Total result: {result}")

if __name__ == "__main__":
    main()

