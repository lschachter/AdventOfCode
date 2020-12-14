def parse_input_file():
    input_file = open('2020/day_10/input.txt', 'r')
    data = list(map(int, input_file.read().split('\n')))
    input_file.close()

    return data

def test_chargers(charger_test):
    data = parse_input_file()
    data.sort()

    return charger_test(data)

def sum_paths(data):
    adapters_by_parent = track_adapters(data)
    for adapter in adapters_by_parent:
        if isinstance(adapters_by_parent[adapter], int):
            continue

        total = 0
        for child in adapters_by_parent[adapter]:
            total += adapters_by_parent[child]

        adapters_by_parent[adapter] = total

    return adapters_by_parent[0]

def track_adapters(data):
    data.insert(0, 0)
    num_adapters = len(data)

    adapters_by_parent = {}
    adapters_by_parent[data[-1]] = 1

    for i in range(num_adapters - 2, -1, -1):
        adapters_by_parent[data[i]] = []
        j = i + 1
        while j < num_adapters and data[j] - data[i] <= 3:
            adapters_by_parent[data[i]].append(data[j])
            j += 1

    return adapters_by_parent

def count_jumps(data):
    jumps = {x: 0 for x in range(1, 4)}

    prev = 0

    for num_jolts in data:
        jump = num_jolts - prev
        jumps[jump] += 1
        prev = num_jolts

    return jumps[1] * (jumps[3] + 1)


print(test_chargers(count_jumps))
print(test_chargers(sum_paths))
