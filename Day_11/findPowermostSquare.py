
class Cell:
	def __init__(self, x, y, GSN):
		self.x = x
		self.y = y
		self.rackID = self.x + 10
		self.GSN = GSN
		self.power = self.setPowerLevel()

	def setPowerLevel(self):
		power = self.rackID * self.y
		power += self.GSN
		power *= self.rackID
		power = getDigit(power, 2)
		power -= 5
		return power

	def __str__(self):
		return str(self.power)


def getDigit(number, index):
	return (number // (10 ** index)) % 10


def main():
	n = 300
	m = 300
	GSN = 7989
	squareHeight = 3
	squareWidth = 3
	
	grid = setInitialGrid(n, m, GSN)
	aux = setAuxGrid(grid)
	# maxIndex, maxSum = sumBySquare(aux, n, m, squareHeight, squareWidth)
	maxIndex, squareSize = findMaxSquareSize(aux, n, m)
	print(maxIndex, squareSize)


def setInitialGrid(n, m, GSN):
	grid = [[Cell(x, y, GSN).power for x in range(m)] for y in range(n)]
	return grid


def setAuxGrid(grid):
	n = len(grid)
	m = len(grid[0])
	aux = [[val for val in row] for row in grid]
	for y in range(1, n):
		aux[y][0] = aux[y - 1][0] + aux[y][0]
	for x in range(1, m):
		aux[0][x] = aux[0][x - 1] + aux[0][x]

	for y in range(1, n):
		rowSum = grid[y][0]
		for x in range(1, m):
			rowSum += grid[y][x]
			aux[y][x] = aux[y - 1][x] + rowSum 

	return aux


def sumBySquare(aux, n, m, height, width):
	heightIndex = height - 1
	widthIndex = width - 1
	maxSum = float('-inf')
	maxIndex = (0,0)
	sums = []
	for y in range(n):
		row = []
		for x in range(m):
			if y < heightIndex or x < widthIndex:
				row.append(float('-inf'))
			elif y == heightIndex and x == widthIndex:
				total = aux[y][x]
				row.append(total)
				if total > maxSum:
					maxSum = total
					maxIndex = (0, 0)
			elif x == widthIndex:
				total = aux[y][x] - aux[y - height][x]
				row.append(total)
				if total > maxSum:
					maxSum = total
					maxIndex = (x - widthIndex, y - heightIndex)
			elif y == heightIndex:
				total = aux[y][x] - aux[y][x - width]
				row.append(total)
				if total > maxSum:
					maxSum = total
					maxIndex = (x - widthIndex, y - heightIndex)
			else:
				total = aux[y][x] - aux[y][x - width] - aux[y - height][x] + aux[y - height][x - width]
				row.append(total)
				if total > maxSum:
					maxSum = total
					maxIndex = (x - widthIndex, y - heightIndex)
		sums.append(row)
	return maxIndex, maxSum


def findMaxSquareSize(aux, n, m):
	totalMaxIndex = (0,0)
	totalMaxSum = float('-inf')
	squareSize = 0
	for i in range(1, n):
		maxIndex, maxSum = sumBySquare(aux, n, m, i, i)
		if maxSum > totalMaxSum:
			totalMaxIndex, totalMaxSum = maxIndex, maxSum
			squareSize = i

	return totalMaxIndex, squareSize


def printGrid(grid):
	for row in grid:
		print(row)




main()
