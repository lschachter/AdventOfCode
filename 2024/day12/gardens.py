data_file = open("input.txt", "r")
data = data_file.read().splitlines()
data = [list(row) for row in data]
data_file.close()


def group_gardens():
    to_try = set()
    seen = set()

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = [(0, 0)]

    perimeter = area = 0
    total = 0

    while queue or to_try:
        if not queue:
            total += perimeter * area
            perimeter = area = 0
            queue.append(to_try.pop())

        i, j = queue.pop(0)
        if (i, j) in seen:
            continue

        area += 1
        seen.add((i, j))
        for x, y in dirs:
            new_i = i + x
            new_j = j + y
            if (new_i, new_j) in seen:
                if data[new_i][new_j] != data[i][j]:
                    perimeter += 1
                continue

            if not (0 <= new_i < len(data) and 0 <= new_j < len(data[0])):
                perimeter += 1
                continue

            if data[new_i][new_j] == data[i][j]:
                queue.append((new_i, new_j))
            else:
                to_try.add((new_i, new_j))
                perimeter += 1

    if area:
        total += area * perimeter

    return total


print(group_gardens())
