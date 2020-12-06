def parse_input_file():
    input_file = open('2020/day_6/input.txt', 'r')
    data = input_file.read().split('\n\n')
    input_file.close()

    return data

def customs_forms():
    data = parse_input_file()

    answer_counts = 0
    for group in data:
        # 'any' for rule 1 (union), 'all' for rule 2 (intersection)
        answer_counts += validate(group, 'all')

    return answer_counts

def validate(group, rule):
    ALL = 'all'
    answers = []
    for line in group.split('\n'):
        answers.append({ch for ch in line})

    return len(set.intersection(*answers)) if rule == ALL else len(set.union(*answers))


print(customs_forms())
