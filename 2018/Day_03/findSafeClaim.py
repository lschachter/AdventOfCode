

def main():

	grid = setGrid()
	claims = open('claims.txt', 'r').read().split('\n')
	claimIDs = {claim.split('@')[0]: True for claim in claims}

	for claim in claims:
		claimID, x, y, w, h = getCleanData(claim)
		grid, claimIDs = addToGrid(claimID, x, y, w, h, grid, claimIDs)

	for claim in claimIDs:
		if claimIDs[claim] == True:
			print(claim)

def setGrid():
	grid = []

	for i in range(1000):
		row = [0] * 1000
		grid.append(row)
	return grid

def getCleanData(claim):
	data = claim.split('@')
	claimID = data[0]

	swathData = data[1]
	xAndData = swathData.split(',')
	x = int(xAndData[0])
	yAndData = xAndData[1].split(':')
	y = int(yAndData[0])
	wAndData = yAndData[1].split('x')
	w = int(wAndData[0])
	h = int(wAndData[1])

	return claimID, x, y, w, h


def addToGrid(claimID, x, y, w, h, grid, claimIDs):
	for i in range(y, y + h):
		for j in range(x, x + w):
			if grid[i][j] != 0:
				claimIDs[grid[i][j]] = False
				claimIDs[claimID] = False
			else:
				grid[i][j] = claimID

	return grid, claimIDs


main()



