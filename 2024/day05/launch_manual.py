from collections import defaultdict

data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()


def check_order():
    rules, orders = data.split("\n\n")

    rules = rules.split("\n")
    rules_dict = defaultdict(list)
    for rule in rules:
        prereq, postreq = list(map(int, rule.split("|")))
        rules_dict[postreq].append(prereq)

    orders = orders.split("\n")
    orders = [[int(num) for num in order.split(",")] for order in orders]

    return check_incorrectly_ordered(orders, rules_dict)


# DOES NOT WORK
def check_incorrectly_ordered(orders, rules_dict):
    invalid_orders = []

    for order in orders:
        is_valid = True
        for i in range(len(order) - 1):
            for j in range(i + 1, len(order)):
                if order[j] in rules_dict[order[i]]:
                    is_valid = False
                    break

            if not is_valid:
                invalid_orders.append(order)
                break

    for order in orders:
        is_valid = make_valid(order, rules_dict)
        num_checks = 1
        while not is_valid:
            is_valid = make_valid(order, rules_dict)
            num_checks += 1
            if num_checks > 100:
                print("fucked up")
                break

    total = 0
    for order in invalid_orders:
        median = len(order) // 2
        total += order[median]

    return total


def make_valid(order, rules_dict):
    for i in range(len(order) - 1):
        for j in range(i + 1, len(order)):
            if order[j] in rules_dict[order[i]]:

                invalid_num = order.pop(i)
                order.insert(j, invalid_num)
                return False

    return True


def check_correctly_ordered(orders, rules_dict):
    total = 0

    for order in orders:
        is_valid = check_validity(order, rules_dict)
        if is_valid:
            median = len(order) // 2
            total += order[median]

    return total


def check_validity(order, rules_dict):
    is_valid = True
    for i in range(len(order) - 1):
        if not is_valid:
            break
        for j in range(i + 1, len(order)):
            if order[j] in rules_dict[order[i]]:
                is_valid = False
                break

    return is_valid


print(check_order())
