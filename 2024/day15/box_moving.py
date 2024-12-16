data_file = open("input.txt", "r")
grid, instructions = data_file.read().split("\n\n")
grid = [list(row) for row in grid.split("\n")]
instructions = "".join(instructions.split("\n"))
data_file.close()


def move_boxes():
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

    i, j = find_start()

    # for row in grid:
    #     print(row)
    # print()

    for move in instructions:
        x, y = directions[move]
        new_i = i + x
        new_j = y + j

        # print(move)

        if grid[new_i][new_j] == "#":  # do each separately then combine
            continue

        elif grid[new_i][new_j] == ".":
            grid[i][j], grid[new_i][new_j] = grid[new_i][new_j], grid[i][j]
            i, j = new_i, new_j
        else:
            # print("hi")
            # print(grid[new_i][new_j])
            a, b = new_i, new_j
            while grid[a][b] not in ["#", "."]:
                a += x
                b += y

            # print(a, b, grid[a][b])
            if grid[a][b] == "#":
                continue

            grid[a][b] = "O"
            grid[i][j] = "."
            grid[new_i][new_j] = "@"
            i, j = new_i, new_j

        # for row in grid:
        #     print(row)
        # print()


def sum_gps_coords():
    move_boxes()

    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                total += (100 * i) + j

    return total


def find_start():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return (i, j)


print(sum_gps_coords())
