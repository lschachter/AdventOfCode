
def main():
	locationStrs = open('locations.txt', 'r').read().split('\n')
	locations = [tuple(int(num) for num in tup.split(',')) for tup in locationStrs]

	maxX = max(locations, key = lambda loc: loc[0])[0]
	maxY = max(locations, key = lambda loc: loc[1])[1]

	namedLocations = {'P' + str(i + 1): locations[i] for i in range(len(locations))}
	grid = setEmptyGrid(maxX,maxY)
	setLocations(grid, namedLocations)

	# getLargestFiniteArea(grid, namedLocations)
	MAX_DIST_SUM = 10000
	getSubXRegion(grid, namedLocations, MAX_DIST_SUM)


def setEmptyGrid(x, y):
	grid = []
	for _ in range(y + 1):
		row = [0] * (x + 2)
		grid.append(row)

	return grid


def setLocations(grid, locations):
	for loc in locations:
		x, y = locations[loc]
		grid[y][x] = loc


def getLargestFiniteArea(grid, namedLocations):
	areas = sumAreas(grid, namedLocations)
	finiteLocs = filterFiniteLocs(grid, namedLocations)
	largestFiniteArea = findLargestFiniteArea(grid, finiteLocs, areas)

	print(largestFiniteArea)


def sumAreas(grid, locations):
	areas = {locName: 1 for locName in locations}
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			countDists, minDist, minLoc = comparePoints(locations, x, y)
			if countDists == 2:
				grid[y][x] = '.'
			elif locations[minLoc] != (x,y):
				areas[minLoc] += 1
				grid[y][x] = minLoc
	return areas


def comparePoints(locations, x, y):
	minDist = float('inf')
	minLoc = None
	countDists = 0
	for loc in locations:
		dist = manhattanDist((x,y), locations[loc])
		if dist < minDist:
			minDist = dist
			minLoc = loc
			countDists = 1
		elif dist == minDist:
			countDists = 2

	return countDists, minDist, minLoc


def manhattanDist(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def filterFiniteLocs(grid, namedLocations):
	locations = set(namedLocations.keys())
	infiniteLocs = findInfiniteLocs(grid)

	finiteLocs = locations - infiniteLocs
	return finiteLocs


def findInfiniteLocs(grid):
	n = len(grid)
	infiniteLocs = set()

	for y in range(n):
		infiniteLocs.add(grid[y][0])
		infiniteLocs.add(grid[y][-1])

	infiniteLocs |= set(grid[0])
	infiniteLocs |= set(grid[-1])

	return infiniteLocs


def findLargestFiniteArea(grid, finiteLocs, areas):
	finiteAreas = {locName: areas[locName] for locName in areas if locName in finiteLocs}
	largestFiniteLoc = max(finiteAreas, key = lambda key: finiteAreas[key])
	return finiteAreas[largestFiniteLoc]


def getSubXRegion(grid, namedLocations, maxDistSum):
	sumDists(grid, namedLocations)
	totalSubMaxDist = countSubXRegion(grid, namedLocations, maxDistSum)
	print(totalSubMaxDist)


def countSubXRegion(grid, namedLocations, maxDistSum):
	totalSubMaxDist = 0
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] < maxDistSum:
				totalSubMaxDist += 1

	return totalSubMaxDist


def sumDists(grid, locations):
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			totalDist = 0
			for loc in locations:
				totalDist += manhattanDist((x,y), locations[loc])
				if totalDist >= 10000:
					break
			grid[y][x] = totalDist

main()