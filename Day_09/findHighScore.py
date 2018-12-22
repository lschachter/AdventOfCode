
class Marble:
	def __init__(self, name):
		self.name = name
		self.left = None
		self.right = None

	def __str__(self):
		left = self.left.name if self.left else "None"
		right = self.right.name if self.right else "None"
		return f'Marble {self.name}: ({left}, {right})'


def main():
	gameInput = open('marbleInput.txt', 'r').read().split()
	numPlayers = int(gameInput[0])
	numMarbles = int(gameInput[-2])

	# numPlayers = 13
	# numMarbles = 7999

	numMarbles = numMarbles * 100
	# printMe(marble, numMarbles)
	scores = playGame(numPlayers, numMarbles)
	print(findHighScore(scores))


def playGame(numPlayers, numMarbles):
	scores = {}
	startingMarble = Marble(0)
	currentMarble = Marble(1)
	startingMarble.right = startingMarble.left = currentMarble
	currentMarble.left = currentMarble.right = startingMarble

	player = 1

	for marbleNum in range(2, numMarbles + 1):
		if marbleNum % 23 == 0:
			addScore(scores, player, marbleNum)
			for i in range(7):
				currentMarble = currentMarble.left
			scores[player] += currentMarble.name
			currentMarble = currentMarble.right
			currentMarble.left = currentMarble.left.left
			currentMarble.left.right = currentMarble
		else:
			newMarble = Marble(marbleNum)
			tempMarble = currentMarble.right.right
			currentMarble.right.right = newMarble
			newMarble.left = currentMarble.right
			newMarble.right = tempMarble
			tempMarble.left	= newMarble
			currentMarble = newMarble
		player = (player + 1) % numPlayers

	return scores


def addScore(scores, player, marbleNum):
	if player in scores:
		scores[player] += marbleNum
	else:
		scores[player] = marbleNum


def printMe(marble, numMarbles):
	for i in range(numMarbles + 1):
		print(marble.name, end=" ")
		marble = marble.right
	print()


def findHighScore(scores):
	return max(scores.values())









'''

def playGame(numPlayers, numMarbles):
	scores = {player: 0 for player in range(numPlayers)}
	currentMarbleIndex = 0
	player = 1
	circle = [0]

	for marbleNum in range(1, numMarbles + 1):
		if marbleNum % 23 == 0:
			scores[player] += marbleNum
			currentMarbleIndex = (currentMarbleIndex - 7) % len(circle)
			scores[player] += circle.pop(currentMarbleIndex)
		else:
			currentMarbleIndex += 2
			if currentMarbleIndex > len(circle):
				currentMarbleIndex = 1	
			circle.insert(currentMarbleIndex, marbleNum)
		player = (player + 1) % numPlayers
	return scores





'''


main()
