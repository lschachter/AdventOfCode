from typing import Dict, List

data_file = open("input.txt", "r")
gates, rules = data_file.read().split("\n\n")
data_file.close()

gates = gates.split("\n")
rules = rules.split("\n")

gates: Dict[str, str] = dict(map(lambda gate: gate.split(": "), gates))
rules: Dict[str, List[str]] = [rule.split() for rule in rules]

# rules by result: result: gate1, gate2, operator
rules = {rule[4]: [rule[0], rule[2], rule[1]] for rule in rules}


def build_number(gates):
    for rule, vals in rules.items():
        gates[rule] = get_gate(*vals)

    gates = list(gates.items())
    gates.sort(key=lambda pair: pair[0])

    num = []
    i = -1
    while gates[i][0].startswith("z"):
        num.append(gates[i][1])
        i -= 1

    return int("".join(num), 2)


def get_gate(gate_1, gate_2, operator):
    right = gates.get(gate_1) or get_gate(*rules[gate_1])
    left = gates.get(gate_2) or get_gate(*rules[gate_2])

    gates[gate_1] = right
    gates[gate_2] = left

    if operator == "AND":
        return "1" if right == "1" and left == "1" else "0"
    if operator == "OR":
        return "1" if right == "1" or left == "1" else "0"
    if operator == "XOR":
        return "1" if set(["1", "0"]) == set([right, left]) else "0"


print(build_number(gates))
