def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_input(input_text):
    rules_section, updates_section = input_text.strip().split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(','))) for update in updates_section.splitlines()]
    return rules, updates

def is_correctly_ordered(rules, update):
    index_map = {page: i for i, page in enumerate(update)}
    return all(index_map[i] < index_map[j] for i, j in rules if i in index_map and j in index_map)

def find_middle_page(update):
    return update[len(update) // 2]

def sum_middle_pages(input_text):
    rules, updates = parse_input(input_text)
    middle_sum = 0
    for update in updates:
        if is_correctly_ordered(rules, update):
            middle_sum += find_middle_page(update)
    return middle_sum

if __name__ == "__main__":
    file_path = "input.txt"
    input_text = read_input(file_path)
    result = sum_middle_pages(input_text)
    print(result)
