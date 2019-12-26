

def main():

	grid = setGrid()
	claims = open('claims.txt', 'r').read().split('\n')

	for claim in claims:
		x, y, w, h = getCleanData(claim)
		grid = addToGrid(x, y, w, h, grid)

	print(countGrid(grid))

def setGrid():
	grid = []

	for i in range(1000):
		row = [0] * 1000
		grid.append(row)
	return grid

def getCleanData(claim):
	data = claim.split('@')[1]
	xAndData = data.split(',')
	x = int(xAndData[0])
	yAndData = xAndData[1].split(':')
	y = int(yAndData[0])
	wAndData = yAndData[1].split('x')
	w = int(wAndData[0])
	h = int(wAndData[1])

	return x, y, w, h


def addToGrid(x, y, w, h, grid):
	for i in range(y, y + h):
		for j in range(x, x + w):
			grid[i][j] += 1

	return grid


def countGrid(grid):
	total = 0

	for row in grid:
		for y in row:
			if y > 1:
				total += 1

	return total

main()



