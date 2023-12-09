data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()

import math

# PARALLELISM BIIIIIITCH


class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.right = right
        self.left = left

    def __str__(self):
        left = self.left if not self.left else self.left.name
        right = self.right if not self.right else self.right.name

        return f"{self.name}: ({left}, {right})"


def puzzle1():
    moves, nodes = data.split("\n\n")
    nodes = nodes.split("\n")

    nodes = {node[:3]: (Node(node[:3]), node[7:10], node[12:-1]) for node in nodes}

    for tup in nodes.values():
        tup[0].left = nodes[tup[1]][0]
        tup[0].right = nodes[tup[2]][0]

    nodes = [node[0] for node in nodes.values()]

    # for node in nodes:
    #     print(node)

    for node in nodes:
        if node.name == "AAA":
            break

    i = 0
    num_steps = 0
    while node.name != "ZZZ":
        if moves[i] == "R":
            node = node.right
        else:
            node = node.left
        i = (i + 1) % len(moves)
        num_steps += 1

    print(num_steps)


# puzzle1()


# taken from https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-the-least-common-multiple
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def puzzle2():
    global find_z  # for multiprocessing

    moves, nodes = data.split("\n\n")
    nodes = nodes.split("\n")

    nodes = {node[:3]: (Node(node[:3]), node[7:10], node[12:-1]) for node in nodes}

    for tup in nodes.values():
        tup[0].left = nodes[tup[1]][0]
        tup[0].right = nodes[tup[2]][0]

    nodes = [node[0] for node in nodes.values()]
    starting_nodes = [node for node in nodes if node.name.endswith("A")]

    def find_z(node):
        num_steps = 0
        i = 0
        while node.name[-1] != "Z":
            if moves[i] == "R":
                node = node.right
            else:
                node = node.left
            i = (i + 1) % len(moves)
            num_steps += 1
        return num_steps

    if __name__ == "__main__":
        from functools import reduce
        import multiprocessing

        pool = multiprocessing.Pool(processes=len(starting_nodes))
        outputs = pool.map(find_z, starting_nodes)

        print(reduce(lcm, outputs))


puzzle2()
