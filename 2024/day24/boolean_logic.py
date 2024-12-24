from typing import List

data_file = open("input.txt", "r")
gates, rules = data_file.read().split("\n\n")
data_file.close()

gates = gates.split("\n")
rules = rules.split("\n")

gates = dict(map(lambda gate: gate.split(": "), gates))
rules = [rule.split() for rule in rules]

# rules by result: result: gate1, gate2, operator
rbr = {rule[4]: [rule[0], rule[2], rule[1]] for rule in rules}


class Node:
    def __init__(self, name):
        self.name = name
        self.requirements: List[Node] = []


def run_gates(gates):
    for rule, vals in rbr.items():
        gates[rule] = "1" if recurse(*vals) else "0"

    gates = list(gates.items())
    gates.sort(key=lambda pair: pair[0])

    num = []
    i = -1
    while gates[i][0].startswith("z"):
        num.append(gates[i][1])
        i -= 1

    return int("".join(num), 2)


def recurse(name1, name2, operator):
    right = gates.get(name1)
    if not right:
        right = recurse(rbr[name1][0], rbr[name1][1], rbr[name1][2])
    left = gates.get(name2)
    if not left:
        left = recurse(rbr[name2][0], rbr[name2][1], rbr[name2][2])

    gates[name1] = "1" if right in [True, "1"] else "0"
    gates[name2] = "1" if left in [True, "1"] else "0"

    if operator == "AND":
        return gates[name1] == "1" and gates[name2] == "1"
    if operator == "OR":
        return gates[name1] == "1" or gates[name2] == "1"
    if operator == "XOR":
        return set(["1", "0"]) == set([gates[name1], gates[name2]])


print(run_gates(gates))
