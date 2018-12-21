class TreeNode:
	def __init__(self, name, header):
		self.name = name
		self.numChildren = header[0]
		self.numMetaData = header[1]
		self.children = []
		self.meta = []
		self.value = 0

	def addChild(self, child):
		self.children.append(child)

	def __str__(self):
		return f'{self.name}: ({self.numChildren}, {self.numMetaData})\
		{[child.name for child in self.children]}, {self.meta} {self.value}'



def main():
	license = open('license.txt', 'r').read()
	# license = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
	license = [int(num) for num in license.split()]
	tree = buildRoot(license)
	
	print(determineRootValue(tree))
	traverseTree(tree)
	# print(sumMetaData(tree))


def buildRoot(license):
	numChildren = license.pop(0)
	numMeta = license.pop(0)
	name = 'A'
	root = TreeNode(name, [numChildren, numMeta])
	return buildTree(root, license, numChildren, 1)


def buildTree(node, license, nodesLeft, level):
	if node.numChildren == 0:
		for i in range(node.numMetaData):
			node.meta.append(license.pop(0))
		return node

	for i in range(node.numChildren):
		numChildren = license.pop(0)
		numMeta = license.pop(0)
		newNode = TreeNode(chr(ord("A") + i + level), [numChildren, numMeta])
		node.addChild(buildTree(newNode, license, nodesLeft, level + 1 + i))
	for i in range(node.numMetaData):
		node.meta.append(license.pop(0))
	return node
		

def sumMetaData(root):
	return sumMetaDataHelper(root, 0)

	
def sumMetaDataHelper(node, total):
	if node.numChildren == 0:
		return total + sum(node.meta)
		
	for child in node.children:
		total = sumMetaDataHelper(child, total)
	return total + sum(node.meta)


def determineRootValue(node):
	if node.numChildren == 0:
		val = sum(node.meta)
		node.value = val
		return val
	else:
		for index in node.meta:
			if index - 1 < node.numChildren:
				child = node.children[index - 1]
				if child.value != 0:
					node.value += child.value
				else:
					node.value += determineRootValue(node.children[index - 1])
		return node.value


def traverseTree(root):
	print(root)
	traverseTreeHelper(root)


def traverseTreeHelper(node):
	for child in node.children:
		print(child)
	for child in node.children:
		traverseTreeHelper(child)



main()