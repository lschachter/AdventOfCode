def parse_input_file():
    input_file = open('2020/day_7/input.txt', 'r')
    data = input_file.read().split('\n')
    input_file.close()

    return data

def process_input(bag_color, search_type):
    bag_rules = parse_input_file()
    bag_color = bag_color.replace(' ', '')

    default_replacements = ['.', 'bags', 'bag', ' ']
    rules = {
        'by_child': {
            'replacements': default_replacements + ['1', '2', '3', '4', '5'],
            'bag_filler': bags_by_child,
            'search': bfs_by_child,
        },
        'by_parent': {
            'replacements': default_replacements,
            'bag_filler': bags_by_parent,
            'search': dfs_by_parent,
        }
    }

    bags = {}
    fill_bags = rules[search_type]['bag_filler']
    for line in bag_rules:
        for replacement in rules[search_type]['replacements']:
            line = line.replace(replacement, '')

        parent, children = line.split('contain')
        children = children.split(',')
        [fill_bags(bags, parent, child) for child in children]

    search = rules[search_type]['search']

    return search(bags, bag_color)

def bags_by_child(bags, parent, child):
    if child != 'noother':
        bags.setdefault(child, set())
        bags[child].add(parent)

def bags_by_parent(bags, parent, child):
    if child != 'noother':
        bags.setdefault(parent, {})
        child_num, clean_child = int(child[0]), child[1:]
        bags[parent][clean_child] = child_num
    else:
        bags[parent] = 0

def bfs_by_child(bags, bag_color):
    bags_to_check = {bag_color}
    bags_checked = set()

    while bags_to_check:
        for i in range(len(bags_to_check)):
            bag = bags_to_check.pop()
            bags_checked.add(bag)
            bags_to_check = bags_to_check.union(bags[bag]) if bag in bags else bags_to_check

    return len(bags_checked) - 1

def dfs_by_parent(bags, bag_color):
    def count_bags_recursive(node):
        if bags[node] == 0:
            return 1, True

        total_bags = 0
        for bag in bags[node]:
            num_bags = bags[node][bag]
            child_bags, child_is_leaf = count_bags_recursive(bag)
            total_bags += (num_bags * child_bags)
            total_bags += num_bags if not child_is_leaf else 0

        return total_bags, False

    bag_count, _ = count_bags_recursive(bag_color)

    return bag_count


print(process_input('shiny gold', 'by_parent'))
