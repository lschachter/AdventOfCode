CHILD_INDEX = 1
PARENT_INDEX = 0

def main():
	# reqs = open('sleighInstructions.txt', 'r').read().split('\n')
	reqs = open('fakeInstructions.txt', 'r').read().split('\n')
	reqs = [req.upper() for req in reqs]
	reqs = [tuple(step[0] for step in req.split('STEP ')[1:]) for req in reqs]
	validSteps = sorted(list(set(step[0] for step in reqs) - set(step[1] for step in reqs)))
	stepsByChildren = sorted(reqs, key = lambda pair: pair[CHILD_INDEX])
	stepsByParents = sorted(reqs, key = lambda pair: pair[PARENT_INDEX])

	childIndeces = mapStartingIndex(stepsByChildren, CHILD_INDEX)
	parentIndeces = mapStartingIndex(stepsByParents, PARENT_INDEX)
			
	order = buildOutput(validSteps, stepsByParents, parentIndeces, stepsByChildren, childIndeces)
	print(order)

	
def mapStartingIndex(steps, sorter):
	startingIndeces = {steps[0][sorter]: 0}
	pointer = 0
	for i in range(1, len(steps)):
		step = steps[i][sorter]
		if step in startingIndeces:
			pointer += 1
		else:
			startingIndeces[step] = i

	return startingIndeces


def buildOutput(validSteps, stepsByParents, parentIndeces, stepsByChildren, childIndeces):
	order = ""

	while validSteps:
		nextStep = validSteps.pop(0)
		order += nextStep
		if nextStep in parentIndeces:
			findValidChildren(nextStep, order, stepsByParents, parentIndeces, stepsByChildren, childIndeces, validSteps)

	return order


def findValidChildren(nextStep, order, stepsByParents, parentIndeces, stepsByChildren, childIndeces, validSteps):
	i = parentIndeces[nextStep]
	childStep = stepsByParents[i]
	while childStep[PARENT_INDEX] == nextStep:
		child = childStep[CHILD_INDEX]
		if isValid(child, order, stepsByChildren, childIndeces):
			validSteps.append(child)
			validSteps.sort()
		i += 1
		if i < len(stepsByParents):
			childStep = stepsByParents[i]
		else:
			break


def isValid(ch, order, stepsByChildren, childIndeces):
	i = childIndeces[ch]
	parentStep = stepsByChildren[i]
	while parentStep[CHILD_INDEX] == ch:
		if parentStep[PARENT_INDEX] not in order:
			return False
		i += 1
		if i < len(stepsByChildren):
			parentStep = stepsByChildren[i]
		else:
			break
	return True

	





	













'''
print(steps)

	stepNodes = {}

	validSteps = sorted(list(set(step[0] for step in steps) - set(step[1] for step in steps)))

	for step in steps:
		reqName = step[0]
		childName = step[1]
		if reqName in stepNodes:
			stepNodes[reqName].append(childName)
		else:
			stepNodes[reqName] = [childName]

x = set()
	for step in validSteps:
		print(step, ":", sorted(stepNodes[step]))
		x |= set(stepNodes[step])


{'B', 'U', 'A', 'Y', 'E', 'Z', 'K', 'T', 'M', 'G', 'O', 'P', 'L', 'J'}
'''


main()