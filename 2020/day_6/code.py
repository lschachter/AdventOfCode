def parse_input_file():
    input_file = open('2020/day_6/input.txt', 'r')
    data = input_file.read().split('\n\n')

    input_file.close()

    return data

def customs_forms(validate):
    data = parse_input_file()

    answer_counts = 0
    for group in data:
        answer_counts += validate(group)

    return answer_counts

def validate_any(group):
    answers = set()
    for line in group.split('\n'):
        [answers.add(ch) for ch in line]

    return len(answers)

def validate_all(group):
    answers = []
    for line in group.split('\n'):
        answers.append({ch for ch in line})

    return len(set.intersection(*answers))


print(customs_forms(validate_all))
