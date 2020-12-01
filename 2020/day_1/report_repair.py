# if we sort them, then we can put one pointer at the front and one at the end
# add those two nums together. if the answer's too big, move the second pointer
# further back into the list. if the answer's too small, move the first pointer
# further forward into the list. end when they sum to 2020 or when they meet,
# in which case there is no answer.

def build_expense_list():
    report = open('expense_report.txt', 'r').read()
    return map(int, report.split('\n'))


def sum_two(k):
    expenses = build_expense_list()
    expenses = sorted(expenses)

    p1 = 0
    p2 = len(expenses) - 1

    while p1 != p2:
        if expenses[p1] + expenses[p2] == k:
            print(expenses[p1], expenses[p2])
            return expenses[p1] * expenses[p2]
        if expenses[p1] + expenses[p2] < k:
            p1 += 1
        else:
            p2 -= 1

    return 0

print(sum_two(2020))