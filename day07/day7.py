file_path = "input.txt"

def read_equations(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def generate_operator_combinations(operator_count):
    if operator_count == 0:
        return [""]
    smaller_combinations = generate_operator_combinations(operator_count - 1)
    all_combinations = []
    for combination in smaller_combinations:
        all_combinations.append(combination + '+')
        all_combinations.append(combination + '*')
    return all_combinations

def evaluate_expression_with_operators(numbers, operators):
    current_result = numbers[0]
    for number, operator in zip(numbers[1:], operators):
        if operator == '+':
            current_result += number
        elif operator == '*':
            current_result *= number
    return current_result

def can_test_value_be_reached(target_value, number_list):
    possible_operator_combinations = generate_operator_combinations(len(number_list) - 1)
    for operator_combination in possible_operator_combinations:
        if evaluate_expression_with_operators(number_list, operator_combination) == target_value:
            return True
    return False
#Functional "Approach" is the GOAT, boys. 3 pure functions right above.

def sum_of_valid_test_values(equation_list):
    total_sum = 0
    for equation in equation_list:
        target_value, number_sequence = equation.split(':')
        target_value = int(target_value)
        number_list = list(map(int, number_sequence.split()))
        if can_test_value_be_reached(target_value, number_list):
            total_sum += target_value
    return total_sum

equations = read_equations(file_path)
calibration_result = sum_of_valid_test_values(equations)
print(f"Total result: {calibration_result}")

