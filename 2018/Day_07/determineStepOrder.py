
def main():
	reqs = open('sleighInstructions.txt', 'r').read().split('\n')
	# reqs = open('fakeInstructions.txt', 'r').read().split('\n')
	reqs = [req.upper() for req in reqs]
	reqs = [tuple(step[0] for step in req.split('STEP ')[1:]) for req in reqs]
	validSteps = sorted(list(set(step[0] for step in reqs) - set(step[1] for step in reqs)))
	steps = buildSteps(reqs)
	
	# order = buildOutput(validSteps, steps)
	# print(order)

	baseSecsPerStep = 61
	numWorkers = 5

	timeSpent = buildInParallel(validSteps, steps, numWorkers, baseSecsPerStep)
	print(timeSpent)


def buildSteps(reqs):
	nodes = {}
	for req in reqs:
		child = req[1]
		parent = req[0]
		if parent in nodes:
			pNode = nodes[parent]
		else:
			pNode = Step(parent)
			nodes[parent] = pNode

		if child in nodes:
			cNode = nodes[child]
		else:
			cNode = Step(child)
			nodes[child] = cNode

		pNode.children.append(cNode)
		cNode.parents.append(pNode)

	return nodes


def buildOutput(validSteps, allSteps):
	order = ""

	while validSteps:
		stepName = validSteps.pop(0)
		order += stepName
		step = allSteps[stepName]
		if step.children:
			addValidChildren(step, order, validSteps)

	return order


def addValidChildren(step, order, validSteps):
	for child in step.children:
		if isValid(child, order):
			validSteps.append(child.name)
			validSteps.sort() # BAD


def isValid(step, order):
	for parent in step.parents:
		if parent.name not in order:
			return False

	return True


class Step:
		def __init__(self, name):
			self.name = name
			self.children = []
			self.parents = []



	
def buildInParallel(validSteps, allSteps, numWorkers, baseSecsPerStep):
	abcs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	secsPerStep = {let: num + baseSecsPerStep for num, let in enumerate(abcs)}

	order = ""
	workers = []
	for i in range(numWorkers):
		worker = Worker(str(i + 1))
		workers.append(worker)

	# print("Second    Worker1    Worker2    Done")
	second = 0
	currentJobs = []

	while validSteps or currentJobs:
		for job in currentJobs:
			worker = job[0]
			stepName = job[1]
			step = allSteps[stepName]

			worker.busyFor -= 1
			if worker.busyFor == 0:
				setWorkerFree(worker)
				order += stepName
				# BAD
				if step.children:
					addValidChildren(step, order, validSteps)

		currentJobs = [job for job in currentJobs if job[0].isWorking]
		currentJobs += startNewSteps(workers, validSteps, secsPerStep)
		# printMe(second, workers[0].currentJob, workers[1].currentJob, order)
		second += 1

	return second - 1


def setWorkerFree(worker):
	worker.isWorking = False
	worker.currentJob = None


def startNewSteps(workers, validSteps, secsPerStep):
	availableWorker = findAvailableWorker(workers)
	newJobs = []

	while len(validSteps) > 0 and availableWorker:
		nextStep = validSteps.pop(0)
		setWorker(availableWorker, nextStep, secsPerStep)
		
		newJobs.append((availableWorker, nextStep))
		availableWorker = findAvailableWorker(workers)

	return newJobs


def printMe(second, worker1, worker2, done):
	print(second, '\t    ', worker1, '\t      ', worker2, '\t  ', done)


def findAvailableWorker(workers):
	for worker in workers:
		if not worker.isWorking:
			return worker
	return False


def setWorker(worker, nextStep, secsPerStep):
	worker.isWorking = True
	worker.currentJob = nextStep
	worker.busyFor = secsPerStep[nextStep]


class Worker:
	def __init__(self, name):
		self.name = name
		self.isWorking = False
		self.currentJob = None
		self.busyFor = 0


	def __str__(self):
		return f'Worker #{self.name}: working ? {self.isWorking} on {self.currentJob} for {self.busyFor} seconds'


main()
