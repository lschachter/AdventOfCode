data_file = open("input.txt", "r")
data = data_file.read().splitlines()
data = [list(row) for row in data]
data_file.close()

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
pointers = {">": ["^", "v"], "^": ["<", ">"], "<": ["^", "v"], "v": ["<", ">"]}


def find_paths():
    i, j = find_start()
    exit_point = (0, 0)

    queue = [(0, ">", i, j)]

    while queue:
        num, pointing, i, j = queue.pop(0)
        for pointer in directions:
            new_i = i + directions[pointer][0]
            new_j = j + directions[pointer][1]

            if pointing == pointer:
                new_num = num + 1
            elif pointer in pointers[pointing]:
                new_num = num + 1001
            else:
                new_num = num + 2001

            if data[new_i][new_j] == "E":
                exit_point = (new_i, new_j)

            if data[new_i][new_j] in [".", "E"] or (
                type(data[new_i][new_j]) == int and new_num < data[new_i][new_j]
            ):
                data[new_i][new_j] = new_num
                queue.append((new_num, pointer, new_i, new_j))

    return data[exit_point[0]][exit_point[1]]


def find_paths2():
    i, j = find_start()
    queue = [(0, ">", i, j)]
    exit_point = (0, 0)

    while queue:
        num, pointing, i, j = queue.pop(0)
        for pointer in directions:
            new_i = i + directions[pointer][0]
            new_j = j + directions[pointer][1]

            if pointing == pointer:
                new_num = num + 1
            elif pointer in pointers[pointing]:
                new_num = num + 1001
            else:
                new_num = num + 2001

            if data[new_i][new_j] == "E":
                exit_point = (new_i, new_j)

            if data[new_i][new_j] in [".", "E"] or (
                type(data[new_i][new_j]) == int and new_num < data[new_i][new_j]
            ):
                data[new_i][new_j] = new_num
                queue.append((new_num, pointer, new_i, new_j))

    return exit_point


def draw_paths():
    exit_point = find_paths2()
    min_path = data[exit_point[0]][exit_point[1]]

    num_steps = 0
    queue = [(min_path, exit_point[0], exit_point[1])]

    for row in data:
        print(row)

    print()

    while queue:
        max_num, i, j = queue.pop(0)
        data[i][j] = "O"
        num_steps += 1
        for pointer in directions:
            new_i = i + directions[pointer][0]
            new_j = j + directions[pointer][1]

            if type(data[new_i][new_j]) != int:
                continue

            if data[new_i][new_j] < max_num:
                queue.append((data[new_i][new_j], new_i, new_j))

    for row in data:
        print(row)

    return num_steps


def find_start():
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "S":
                return (i, j)


# print(find_paths())
print(draw_paths())
