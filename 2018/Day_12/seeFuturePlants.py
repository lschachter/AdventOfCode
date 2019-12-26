

def main():
	notes = open('notes.txt', 'r').read().split('\n')
	initialState = notes.pop(0).split(':')[1].strip()
	addition = 1000
	initialState = ('.' * addition) + initialState + ('.' * 2000)
	notes.pop(0)
	notes = getNotes(notes)
	startingIndex = -1 * addition
	numGens = 20
	# printDiagram(initialState, notes, numGens)
	# finalState = runGens(initialState, notes, numGens)
	# potSum = sumPotIndexes(finalState, startingIndex)
	patternN = 2000
	n = 50000000000
	repeat, finalState = findPattern(initialState, notes, startingIndex, patternN)
	
	print(((n - patternN) * repeat) + sumPotIndexes(finalState, startingIndex))

	

	

def getNotes(noteList):
	notes = [row.split('=>') for row in noteList]
	notes = set(row[0].strip() for row in notes if row[1].strip() == "#")
	return notes


def printDiagram(state, notes, numGens):
	space = ' ' * 9
	print(f'{space}0{space}10{space}20{space}30')
	for i in range(numGens):
		printRow(i, state)
		state = updateState(state, notes)
	printRow(i + 1, state)


def printRow(gen, state):
	pad = '' if gen >= 10 else ' '
	print(f'{gen}: {pad}{state}')


def updateState(state, notes):
	lenState = len(state)
	newState = ['.'] * lenState

	for i in range(lenState - 4):
		if state[i: i + 5] in notes:
			newState[i + 2] = "#"

	return ''.join(newState)


def runGens(state, notes, numGens):
	for i in range(numGens):
		state = updateState(state, notes)
	return state


def sumPotIndexes(finalState, startingIndex):
	plantPotSum = 0
	for i in range(len(finalState)):
		if finalState[i] == "#":
			plantPotSum += (i + startingIndex)

	return plantPotSum


def findPattern(state, notes, startingIndex, patternN):
	potSum = 0
	diffs = {}

	for i in range(patternN):
		state = updateState(state, notes)
		lastPotSum = potSum
		potSum = sumPotIndexes(state, startingIndex)
		diff = potSum - lastPotSum
		# print(potSum, diff)
		if diff > 0:
			if diff in diffs:
				diffs[diff].append(i)
			else:
				diffs[diff] = [i]

	return max(diffs, key = lambda key: len(diffs[key])), state


main()
