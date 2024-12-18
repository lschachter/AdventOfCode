data_file = open("input.txt", "r")
data = data_file.read().splitlines()
data = [tuple(map(lambda num: int(num), line.split(","))) for line in data]
data_file.close()


def find_first_failure():
    size = 70
    seen = set()
    z = 1024
    for x, y in data[:z]:
        seen.add((y, x))

    steps = find_path(size, seen.copy())
    while steps != -1:
        seen.add((data[z][1], data[z][0]))
        z += 1
        steps = find_path(size, seen.copy())

    return f"{data[z - 1][0]},{data[z - 1][1]}"


def find_path(size, seen):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [(0, 0, 0)]

    while queue:
        steps, i, j = queue.pop(0)
        if (i, j) == (size, size):
            return steps

        seen.add((i, j))

        for x, y in dirs:
            new_i = i + x
            new_j = j + y

            if 0 <= new_i <= size and 0 <= new_j <= size and (new_i, new_j) not in seen:
                queue.append((steps + 1, new_i, new_j))
                seen.add((new_i, new_j))

    return -1


print(find_first_failure())
