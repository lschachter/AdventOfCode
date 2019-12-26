
def findRepeat():

	inStr = open('freqInput.txt', 'r').read()
	inLst = inStr.split()

	inLst = [int(x) for x in inLst]


	freqs = []
	curFreq = 0
	found = False

	while not found:
		for x in inLst:
			curFreq += x
			if curFreq in freqs:
				found = True
				break

			freqs.append(curFreq)

	return curFreq

print(findRepeat())