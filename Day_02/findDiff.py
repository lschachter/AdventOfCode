
def findLetters():
	ids = open('idInput.txt', 'r').read().split()

	j = 1

	for boxID1 in ids[:-1]:
		for boxID2 in ids[j:]:
			if isValid(boxID1, boxID2):
				return findCommon(boxID1, boxID2)
		j += 1


def isValid(id1, id2):
	diffs = 0
	idLen = len(id1)

	for i in range(idLen):
		if id1[i] != id2[i]:
			if diffs >= 1:
				return False
			diffs += 1

	return True


def findCommon(id1, id2):
	idLen = len(id1)
	output = ""

	for i in range(idLen):
		if id1[i] == id2[i]:
			output += id1[i]

	return output

print(findLetters())