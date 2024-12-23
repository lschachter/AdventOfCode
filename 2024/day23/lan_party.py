from collections import defaultdict
from typing import Dict, Set

data_file = open("input.txt", "r")
data = list(map(lambda conn: conn.split("-"), data_file.read().splitlines()))


def count_lan():
    connections = defaultdict(list)

    for conn1, conn2 in data:
        connections[conn1].append(conn2)
        connections[conn2].append(conn1)

    tri_conns = set()
    num_t_conns = 0

    for comp, conns in connections.items():
        for conn in conns:
            intersection = set(conns).intersection(set(connections[conn]))
            for overlap in intersection:

                combo = tuple(sorted([comp, conn, overlap]))
                if combo not in tri_conns and (
                    comp.startswith("t")
                    or conn.startswith("t")
                    or overlap.startswith("t")
                ):
                    num_t_conns += 1
                    tri_conns.add(combo)

    return num_t_conns


print(count_lan())


class Node:
    def __init__(self, name):
        self.name: str = name
        self.connections: Set[Node] = set()

    def __str__(self):
        return self.name


def count_biggest_lan():
    nodes: Dict[str, Node] = {}

    for name1, name2 in data:
        new_node = nodes.get(name1, Node(name1))
        next_node = nodes.get(name2, Node(name2))
        new_node.connections.add(next_node)
        next_node.connections.add(new_node)
        nodes[name1] = new_node
        nodes[name2] = next_node
