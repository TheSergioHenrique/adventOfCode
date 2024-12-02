filename = 'input.txt'  # Usando um nome de arquivo relativo

def read_file(filename):
    left,right = [], []
    with open(filename) as file:
        for line in file:
            values = line.split()
            left.append(int(values[0]))
            right.append(int(values[1]))
    left.sort()
    right.sort()
    return left, right

def calculate_similarity_score(left, right):
    similarity_score = 0
    for l_value in left:
        count = right.count(l_value)
        similarity_score += l_value * count
    return similarity_score

# Main logic
left, right = read_file(filename)
similarity_score = calculate_similarity_score(left, right)
print(f"Similarity score: {similarity_score}")
