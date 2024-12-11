data_file = open("input.txt", "r")
data = data_file.read().splitlines()
data = [list(row) for row in data]
data_file.close()


def find_xmas_s():
    starts = find_starts()
    nexts = {"X": "M", "M": "A", "A": "S"}
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    total = 0

    for i, j in starts:
        for x, y in dirs:
            current_ch = "X"
            new_i = i + x
            new_j = j + y
            while 0 <= new_i < len(data) and 0 <= new_j < len(data[0]):
                current_ch = nexts[current_ch]
                if current_ch == "S" and data[new_i][new_j] == "S":
                    total += 1
                    break
                if data[new_i][new_j] != current_ch:
                    break
                new_i = new_i + x
                new_j = new_j + y

    return total


def find_starts():
    starts = []

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "X":
                starts.append((i, j))

    return starts


print(find_xmas_s())
