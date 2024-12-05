data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()


def puzzle1():
    grid = data.split("\n")
    grid = [[letter for letter in line] for line in grid]
    starting_x = 0
    starting_y = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                starting_x = x
                starting_y = y

    q = [(starting_x, starting_y, 0, (0, 0))]

    dirs = {
        (1, 0): ["-", "7", "J"],
        (0, -1): ["|", "7", "F"],
        (-1, 0): ["-", "F", "L"],
        (0, 1): ["|", "L", "J"],
    }

    places = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}

    links = {
        "-": ["left", "right"],
        "|": ["up", "down"],
        "7": ["left", "down"],
        "J": ["left", "up"],
        "L": ["right", "up"],
        "F": ["right", "down"],
        "S": ["left", "right", "up", "down"],
    }

    while q:
        x, y, num_steps, prev_direction = q.pop()
        next_steps = links[grid[y][x]]

        grid[y][x] = num_steps
        moves = []
        for move in next_steps:
            if places[move] != prev_direction:
                moves.append(places[move])

        for direction in moves:
            new_x, new_y = x + direction[0], y + direction[1]
            if not 0 <= new_x < len(grid[0]) or not 0 <= new_y < len(grid):
                continue
            if grid[new_y][new_x] == 0:
                q = []
                break

            if grid[new_y][new_x] not in dirs[direction]:
                continue

            q.append(
                (new_x, new_y, num_steps + 1, (direction[0] * -1, direction[1] * -1))
            )

    print((num_steps + 1) // 2)


# puzzle1()

def puzzle2():
    
