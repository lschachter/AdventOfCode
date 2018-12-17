
def main():
	entries = open('schedule.txt', 'r').read().split('\n')
	entries.sort()

	guardLog = fillGuardLog(entries)

	sleepiestGuard, maxMinute = findSleepiestGuard(guardLog)
	print(sleepiestGuard * maxMinute)

	consistentGuard, consistentMin = findConsistentGuard(guardLog)
	print(consistentGuard * consistentMin)


def fillGuardLog(entries):
	guardLog = {}
	# {guard#: [sumAsleep, {eachMin: daysSlept}]}

	numEntries = len(entries)
	i = 1
	guardID = int(entries[0].split('#')[1].split()[0])

	while i < numEntries:
		entry = entries[i]
		if '#' in entry:
			guardID = int(entry.split('#')[1].split()[0])
			i += 1

		else:
			totalSleep, minsSlept = sumSleep(entry, entries[i+1])
			addToGuardLog(guardLog, guardID, totalSleep, minsSlept)
			i += 2

	return guardLog


def sumSleep(entry1, entry2):
	startSleep = int(entry1.split(':')[1][:2])
	endSleep = int(entry2.split(':')[1][:2])

	totalSleep = endSleep - startSleep
	minsSlept = range(startSleep, endSleep)

	return totalSleep, minsSlept


def addToGuardLog(guardLog, guardID, totalSleep, minsSlept):
	if guardID in guardLog:
		guardLog[guardID][0] += totalSleep
		guardLog[guardID][1] = updateMinsSlept(guardLog[guardID][1], minsSlept)
		
	else:
		guardLog[guardID] = [totalSleep]
		guardLog[guardID].append({minute: 1 for minute in minsSlept})


def updateMinsSlept(allMinutesSlept, minsSlept):
	for minute in minsSlept:
		if minute in allMinutesSlept:
			allMinutesSlept[minute] += 1
		else:
			allMinutesSlept[minute] = 1

	return allMinutesSlept


def findSleepiestGuard(guardLog):
	maxGuard = max(guardLog, key = lambda key: guardLog[key][0])
	allMinutesSlept = guardLog[maxGuard][1]
	maxMinute = max(allMinutesSlept, key = lambda key: allMinutesSlept[key])

	return maxGuard, maxMinute


def findConsistentGuard(guardLog):
	guardLogList = list(guardLog.items())

	maxGuard = 0
	maxTotalMinute = (0,0)

	for i in range(len(guardLogList)):
		allMinutesSlept = guardLogList[i][1][1]
		maxMinute = max(allMinutesSlept, key = lambda key: allMinutesSlept[key])
		if allMinutesSlept[maxMinute] > maxTotalMinute[1]:
			maxGuard = guardLogList[i][0]
			maxTotalMinute = (maxMinute, allMinutesSlept[maxMinute])

	return maxGuard, maxTotalMinute[0]

main()
