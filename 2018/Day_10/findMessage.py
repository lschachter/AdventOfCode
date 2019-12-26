
class Light:
	def __init__(self, position, velocity):
		self.currentPos = position
		self.velocity = velocity

	def getNextPos(self):
		x, y = self.currentPos
		changeX, changeY = self.velocity
		newPos = (x + changeX, y + changeY)
		self.currentPos = newPos
		return newPos


def main():
	lightMovement = open('lights.txt', 'r')
	lights = getStartingLights(lightMovement)
	seeFinalPosition(lights)


def getStartingLights(lightMovement):
	lightMovement = lightMovement.read().split('\n')
	lights = []
	light = lightMovement[0]
	pos, vel = light.split('velocity')
	posStart, posEnd = pos.index('<') + 1, pos.index('>')
	velStart, velEnd = vel.index('<') + 1, vel.index('>')

	for light in lightMovement:
		pos, vel = light.split('velocity')
		pos = pos[posStart: posEnd]
		pos = pos.split(',')
		pos = (int(pos[0]), int(pos[1]))
		vel = vel[velStart: velEnd]
		vel = vel.split(',')
		vel = (int(vel[0]), int(vel[1]))
		light = Light(pos, vel)
		lights.append(light)

	return lights


def seeFinalPosition(lights):
	fontHeight = 10
	currentHeight = getHeightDiff([light.currentPos for light in lights])
	sec = 0

	while currentHeight > fontHeight:
		positions = [light.getNextPos() for light in lights]
		currentHeight = getHeightDiff(positions)
		sec += 1

	print(sec)
	mapGrid(positions)


def getHeightDiff(positions):
	ys = [pos[1] for pos in positions]
	return max(ys) - min(ys)


def mapGrid(positions):
	xs = [pos[0] for pos in positions]
	minX = min(xs)
	maxX = max(xs)
	ys = [pos[1] for pos in positions]
	minY = min(ys)
	maxY = max(ys)

	grid = []
	for i in range(minY, maxY + 1):
		row = [' '] * (maxX - minX + 1)
		grid.append(row)

	for x, y in positions:
		grid[y - minY][x - minX] = '#'

	for row in grid:
		print(''.join(row))


main()