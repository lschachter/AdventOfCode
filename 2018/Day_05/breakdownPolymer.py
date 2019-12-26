
def main():
	polymer = open('polymer.txt', 'r').read()
	polymerList = list(polymer)

	minPolymer = breakdownPolymer(polymerList)
	print(len(minPolymer))

	minPolymer = findSmallestPolymer(polymer)
	print(minPolymer)


def breakdownPolymer(polymer):
	polyLen = len(polymer)
	pointer = 0

	while pointer < polyLen - 1:
		if polymer[pointer] == flipped(polymer[pointer + 1]):
			polymer.pop(pointer)
			polymer.pop(pointer)
			polyLen -= 2
			pointer = max(0, pointer - 1)
		else:
			pointer += 1

	return polymer


def flipped(char):
	return char.upper() if char.islower() else char.lower()


def findSmallestPolymer(polymer):
	units = set(polymer.lower())

	minPolymer = len(polymer)
	minEl = polymer[0]

	for unit in units:
		newPolymer = polymer.replace(unit, "")
		newPolymer = newPolymer.replace(unit.upper(), "")
		lenNewPolymer = len(breakdownPolymer(list(newPolymer)))
		if lenNewPolymer < minPolymer:
			minPolymer = lenNewPolymer
			minEl = unit

	return minPolymer

main()












