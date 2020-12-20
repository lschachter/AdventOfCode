import math


def turn_right(compass_facing):
    return compass_facing.right

def turn_left(compass_facing):
    return compass_facing.left


dirs = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}
turns = {'R': turn_right, 'L': turn_left}


class CompassFacing:
    def __init__(self, facing):
        self.facing = facing

    def set_neighbors(self, right, left):
        self.right = right
        self.left = left


def parse_input_file():
    input_file = open('2020/day_12/input.txt', 'r')
    data = input_file.read().split('\n')

    data = [(line[0], int(line[1:])) for line in data]
    input_file.close()

    return data

def navigate_ferry1(compass):
    data = parse_input_file()

    start = (0, 0)
    x, y = 0, 0

    for step in data:
        direction, amount = step
        if direction in dirs:
            x += (dirs[direction][0] * amount)
            y += (dirs[direction][1] * amount)
        elif direction == 'F':
            x += (dirs[compass.facing][0] * amount)
            y += (dirs[compass.facing][1] * amount)
        else:
            num_turns = amount // 90
            for i in range(num_turns):
                compass = turns[direction](compass)

    return manhattan_distance(start, (x, y))

def navigate_ferry():
    data = parse_input_file()

    start = (0, 0)
    wx, wy = 10, 1
    x, y = 0, 0

    for step in data:
        direction, amount = step
        diff_x, diff_y = (wx - x), (wy - y)
        if direction in dirs:
            wx += (dirs[direction][0] * amount)
            wy += (dirs[direction][1] * amount)
        elif direction == 'F':
            x += (diff_x * amount)
            y += (diff_y * amount)

            wx = x + diff_x
            wy = y + diff_y
        else:
            amount = amount if direction == 'L' else (amount * -1)
            wx, wy = rotate((x, y), (wx, wy), amount)

    return manhattan_distance(start, (x, y))

def rotate(origin, point, degrees):
    ox, oy = origin
    px, py = point
    angle = math.radians(degrees)

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy


def manhattan_distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def main():
    east = CompassFacing('E')
    west = CompassFacing('W')
    north = CompassFacing('N')
    south = CompassFacing('S')
    east.set_neighbors(south, north)
    west.set_neighbors(north, south)
    north.set_neighbors(east, west)
    south.set_neighbors(west, east)

    print(navigate_ferry())


main()
