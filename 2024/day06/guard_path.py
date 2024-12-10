data_file = open("input.txt", "r")
data = data_file.read().splitlines()
data = [list(row) for row in data]
data_file.close()


def mark_path():
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    moves = {"^": ">", ">": "v", "v": "<", "<": "^"}

    is_found = False
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] in directions:
                is_found = True
                break
        if is_found:
            break

    curr_dir = data[row][col]
    movement = directions[curr_dir]

    total = 0

    while 0 <= row < len(data) and 0 <= col < len(data[0]):
        if data[row][col] != "#":
            if data[row][col] != "X":
                total += 1
                data[row][col] = "X"

            row += movement[0]
            col += movement[1]
        else:
            row -= movement[0]
            col -= movement[1]
            curr_dir = moves[curr_dir]
            movement = directions[curr_dir]

    # for row in data:
    #     print(row)
    return total


print(mark_path())
