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

def fix_update(rules, update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if any(rule == (update[j], update[i]) for rule in rules):
                update[i], update[j] = update[j], update[i]
    return update

def process_updates(rules, updates):
    valid_sum = 0
    fixed_sum = 0
    for update in updates:
        if is_correctly_ordered(rules, update):
            valid_sum += find_middle_page(update)
        else:
            fixed_sum += find_middle_page(fix_update(rules, update))
    return valid_sum, fixed_sum

if __name__ == "__main__":
    file_path = "input.txt"
    rules, updates = parse_input(read_input(file_path))
    valid_sum, fixed_sum = process_updates(rules, updates)
    print(fixed_sum)
