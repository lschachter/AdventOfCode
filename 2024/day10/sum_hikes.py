data_file = open("input.txt", "r")
data = data_file.read().splitlines()
data = [list(map(int, row)) for row in data]
data_file.close()


def find_viable_hikes():
    starts = find_starts()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    total = 0

    for start, i, j in starts:
        seen = set()
        stack = [(start, i, j)]

        while stack:
            num, prev_i, prev_j = stack.pop()
            for x, y in dirs:
                new_i = prev_i + x
                new_j = prev_j + y
                if (new_i, new_j) in seen:
                    continue
                if 0 <= new_i < len(data) and 0 <= new_j < len(data[0]):
                    if data[new_i][new_j] != num + 1:
                        continue
                    if num + 1 == 9:
                        total += 1
                    else:
                        stack.append((data[new_i][new_j], new_i, new_j))
                    seen.add((new_i, new_j))

    return total


def find_ratings():
    queue = find_starts()
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    total = 0

    while queue:
        num, i, j = queue.pop(0)
        new_num = num + 1
        for x, y in dirs:
            new_i = i + x
            new_j = j + y
            if 0 <= new_i < len(data) and 0 <= new_j < len(data[0]):
                if data[new_i][new_j] != new_num:
                    continue
                if new_num == 9:
                    total += 1
                else:
                    queue.append((data[new_i][new_j], new_i, new_j))

    return total


def find_starts():
    queue = []

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                queue.append((data[i][j], i, j))

    return queue


print(find_ratings())
