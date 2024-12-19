from collections import defaultdict

data_file = open("input.txt", "r")
data = data_file.read().splitlines()
data_file.close()


def set_robots(data):
    robots = {}
    data = [line.split() for line in data]
    data = [list(map(lambda item: item.split("=")[1], line)) for line in data]

    for i, line in enumerate(data):
        pos = tuple(map(int, line[0].split(",")))
        vel = tuple(map(int, line[1].split(",")))
        robots[i] = {"pos": pos, "vel": vel}

    return robots


def build_grid(data):
    robots = set_robots(data)
    h, w = 103, 101
    quadrants = defaultdict(int)

    for robot in robots.values():
        x, y = robot["pos"][1], robot["pos"][0]
        vx, vy = (robot["vel"][1] * 100) % h, (robot["vel"][0] * 100) % w
        i, j = (x + vx) % h, (y + vy) % w

        if j == w // 2 or i == h // 2:
            continue

        quadrant = 0
        if j > w // 2:
            quadrant += 1
        if i > h // 2:
            quadrant += 2

        quadrants[quadrant] += 1

    safety_factor = 1
    for q in quadrants.values():
        safety_factor *= q

    return safety_factor


print(build_grid(data))
