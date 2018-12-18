locs = open('locations.txt', 'r').read().split('\n')

locs = [tuple(int(num) for num in tup.split(',')) for tup in locs]

locs.sort(key = lambda pair: pair[1])
locs.sort()

sortedLocs = open('sortedLocs.txt', 'w')

for loc in locs:
	sortedLocs.write(str(loc))
	sortedLocs.write('\n')
