# if we sort them, then we can put one pointer at the front and one at the end
# add those two nums together. if the answer's too big, move the second pointer
# further back into the list. if the answer's too small, move the first pointer
# further forward into the list. end when they sum to 2020 or when they meet,
# in which case there is no answer.

def build_expense_list():
    report_file = open('2020/day_1/expense_report.txt', 'r')
    expenses = list(map(int, report_file.read().split('\n')))

    report_file.close()
    return expenses


def sum_two(k, expenses):
    expenses = sorted(expenses)

    p1 = 0
    p2 = len(expenses) - 1

    while p1 != p2:
        if expenses[p1] + expenses[p2] == k:
            return expenses[p1] * expenses[p2]
        if expenses[p1] + expenses[p2] < k:
            p1 += 1
        else:
            p2 -= 1

    return 0

# same idea but gonna be much slower-- you have to check each pair against a number between them,
# so you have to do the same process as above, but n times (n being the number of values in the list)
def sum_three(k, expenses):
    expenses = sorted(expenses)
    num_expenses = len(expenses)

    for i in range(num_expenses):
        p1 = 0
        p2 = i + 1
        p3 = len(expenses) - 1

        while p1 < p3:
            if expenses[p1] + expenses[p2] + expenses[p3] == k:
                return expenses[p1] * expenses[p2] * expenses[p3]
            if expenses[p1] + expenses[p2] + expenses[p3] < k:
                p1 += 1
            else:
                p3 -= 1

    return 0


expenses = build_expense_list()
# print(sum_two(2020, expenses))
# print(sum_three(2020, expenses))
