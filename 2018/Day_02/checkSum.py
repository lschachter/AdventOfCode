

def checksum():
	twos = 0
	threes = 0

	ids = open('idInput.txt', 'r').read().split()

	for boxID in ids:
		letters = {}

		for letter in boxID:
			if letter in letters:
				letters[letter] += 1
			else:
				letters[letter] = 1

		vals = letters.values()
		if 2 in vals:
			twos += 1
		if 3 in vals:
			threes += 1

	return twos * threes


print(checksum())



