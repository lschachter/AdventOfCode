import math

MOVES = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def manhattanDist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def buildPath(path):
    origin = (0,0)
    currStart = list(origin)
    pathPoints = {}
    for move in path:
        x, y, xStep, yStep = getAxisData(move)
        for i in range(currStart[0] + xStep, currStart[0] + x + xStep, xStep):
            current = tuple([i, currStart[1]])
            pathPoints[current] = manhattanDist(origin, current)
        for i in range(currStart[1] + yStep, currStart[1] + y + yStep, yStep):
            current = tuple([currStart[0], i])
            pathPoints[current] = manhattanDist(origin, current)

        currStart[0] += x
        currStart[1] += y
    return pathPoints

def findIntersection(pathPoints, path2):
    minIntersection = math.inf
    currStart = [0,0]
    for move in path2:
        x, y, xStep, yStep = getAxisData(move)
        for i in range(currStart[0] + xStep, currStart[0] + x + xStep, xStep):
            current = tuple([i, currStart[1]])
            if current in pathPoints:
                minIntersection = min(minIntersection, pathPoints[current])
        for i in range(currStart[1] + yStep, currStart[1] + y + yStep, yStep):
            current = tuple([currStart[0], i])
            if current in pathPoints:
                minIntersection = min(minIntersection, pathPoints[current])
        
        currStart[0] += x
        currStart[1] += y
    return minIntersection

def getAxisData(move):
    direction, steps = move[0], int(move[1:])
    x = steps * MOVES[direction][0]
    y = steps * MOVES[direction][1]
    xStep = MOVES[direction][0] if x else 1
    yStep = MOVES[direction][1] if not x else 1
    return x, y, xStep, yStep


def countPath(path):
    origin = (0,0)
    currStart = list(origin)
    steps = 0
    pathPoints = {}
    for move in path:
        x, y, xStep, yStep = getAxisData(move)
        for i in range(currStart[0] + xStep, currStart[0] + x + xStep, xStep):
            current = tuple([i, currStart[1]])
            steps += 1
            pathPoints[current] = steps
        for i in range(currStart[1] + yStep, currStart[1] + y + yStep, yStep):
            current = tuple([currStart[0], i])
            steps += 1
            pathPoints[current] = steps

        currStart[0] += x
        currStart[1] += y
    return pathPoints

def findSmallestSum(pathPoints, path2):
    minIntersection = math.inf
    currStart = [0,0]
    steps = 0
    for move in path2:
        x, y, xStep, yStep = getAxisData(move)
        for i in range(currStart[0] + xStep, currStart[0] + x + xStep, xStep):
            current = tuple([i, currStart[1]])
            steps += 1
            if current in pathPoints:
                minIntersection = min(minIntersection, pathPoints[current] + steps)
        for i in range(currStart[1] + yStep, currStart[1] + y + yStep, yStep):
            current = tuple([currStart[0], i])
            steps += 1
            if current in pathPoints:
                minIntersection = min(minIntersection, pathPoints[current] + steps)
        
        currStart[0] += x
        currStart[1] += y
    return minIntersection

def main():
    paths = open("wire_paths.txt", "r").readlines()
    path1 = paths[0].split(',')
    path2 = paths[1].split(',')
    pathPoints = countPath(path1)

    # pathPoints = buildPath(path1)
    # minIntersection = findIntersection(pathPoints, path2)
    # print(minIntersection)
    
    minIntersection = findSmallestSum(pathPoints, path2)
    print(minIntersection)

main()