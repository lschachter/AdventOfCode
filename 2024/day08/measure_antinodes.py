from collections import defaultdict

data_file = open("input.txt", "r")
data = data_file.read().splitlines()
data = [list(row) for row in data]
data_file.close()


def find_antinodes():
    node_positions = defaultdict(list)

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != ".":
                node_positions[data[i][j]].append((i, j))

    antinodes = set()

    for node_type in node_positions:
        nodes = node_positions[node_type]
        if len(nodes) < 2:
            continue

        for x in range(len(nodes)):
            node = nodes[x]
            for y in range(x + 1, len(nodes)):
                next_node = nodes[y]

                x_diff = abs(node[0] - next_node[0])
                y_diff = abs(node[1] - next_node[1])

                # x's will always be in order because they were collected in order
                i = node[0] - x_diff
                j = node[1] - y_diff if node[1] < next_node[1] else node[1] + y_diff

                if 0 <= i < len(data) and 0 <= j < len(data[0]):
                    antinodes.add((i, j))

                i = next_node[0] + x_diff
                j = (
                    next_node[1] + y_diff
                    if node[1] < next_node[1]
                    else next_node[1] - y_diff
                )

                if 0 <= i < len(data) and 0 <= j < len(data[0]):
                    antinodes.add((i, j))

    return len(antinodes)


def find_antinodes_with_harmony():
    node_positions = defaultdict(list)

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != ".":
                node_positions[data[i][j]].append((i, j))

    antinodes = set()

    for node_type in node_positions:
        nodes = node_positions[node_type]
        if len(nodes) < 2:
            continue

        for x in range(len(nodes)):
            node = nodes[x]
            for y in range(x + 1, len(nodes)):
                next_node = nodes[y]

                x_diff = abs(node[0] - next_node[0])
                y_diff = abs(node[1] - next_node[1])

                # x's will always be in order because they were collected in order
                i, j = node
                while 0 <= i < len(data) and 0 <= j < len(data[0]):
                    antinodes.add((i, j))

                    i = i - x_diff
                    j = j - y_diff if node[1] < next_node[1] else j + y_diff

                i, j = next_node
                while 0 <= i < len(data) and 0 <= j < len(data[0]):
                    antinodes.add((i, j))

                    i = i + x_diff
                    j = j + y_diff if node[1] < next_node[1] else j - y_diff

    return len(antinodes)


# print(find_antinodes())
print(find_antinodes_with_harmony())
