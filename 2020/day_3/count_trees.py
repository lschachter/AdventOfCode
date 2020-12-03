def parse_map():
    map_file = open('2020/day_3/map.text', 'r')
    tree_map = map_file.read().split('\n')

    map_file.close()

    return tree_map


def count_trees(x, y):
    TREE = '#'
    tree_map = parse_map()

    # ok so while there are rows left, i think just mod by the length of the column?
    num_rows = len(tree_map)
    num_cols = len(tree_map[0])

    i = 0
    j = 0

    trees = 0

    while i < num_rows:
        trees += 1 if tree_map[i][j] == TREE else 0
        i += y
        j = (j + x) % num_cols

    return trees


# print(count_trees(3, 1))

def check_slopes():
    slopes = {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}

    total = 1

    for slope in slopes:
        total *= count_trees(slope[0], slope[1])

    return total


print(check_slopes())
