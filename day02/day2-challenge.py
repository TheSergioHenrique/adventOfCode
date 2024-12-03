filename = 'input.txt'

def read_file(filename):
    reports = []
    with open(filename) as file:
        for line in file:
            # Certifique-se de que a linha é tratada como string antes de dividir
            if isinstance(line, str):
                report = list(map(int, line.split()))  # Converte para inteiros
                reports.append(report)
    return reports


def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if all(1 <= diff <= 3 for diff in differences):
        return True
    elif all(-3 <= diff <= -1 for diff in differences):
        return True
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            modified_differences = [modified_report[j + 1] - modified_report[j] for j in range(len(modified_report) - 1)]

            if all(1 <= diff <= 3 for diff in modified_differences) or \
               all(-3 <= diff <= -1 for diff in modified_differences):
                return True
        return False
    
filename = 'input.txt'
reports = read_file(filename)
safe_reports_count = sum(is_safe(report) for report in reports)

print(f"Number of safe reports: {safe_reports_count}")