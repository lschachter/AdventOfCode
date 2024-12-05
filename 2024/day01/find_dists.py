from collections import Counter

data_file = open("input.txt", "r")
data = data_file.read().split("\n")
data_file.close()


def build_lists():
    left = []
    right = []

    for row in data:
        row = row.split()
        left.append(int(row[0]))
        right.append(int(row[1]))

    return left, right


def find_dist():
    left, right = build_lists()
    left.sort()
    right.sort()

    dists = 0
    for i in range(len(left)):
        dists += abs(left[i] - right[i])

    return dists


def find_similarities():
    left, right = build_lists()

    right_counter = Counter(right)

    score = 0

    for num in left:
        score += num * right_counter.get(num, 0)

    return score


# print(find_dist())
print(find_similarities())
