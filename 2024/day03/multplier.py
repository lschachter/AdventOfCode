data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()


def run_dos(data):
    data = data.split("do()")
    data = map(lambda x: x.split("don't()")[0], data)

    return simple_multiplier("".join(data))


def simple_multiplier(data):
    data = data.split("mul(")
    data = list(map(lambda x: x.split(")"), data))

    total = 0
    for items in data:
        if items[0][0].isdigit() and items[0][-1].isdigit():
            if " " not in items[0]:
                nums = items[0].split(",")
                if len(nums) > 2:
                    continue
                try:
                    total += int(nums[0]) * int(nums[1])
                except ValueError:
                    continue

    return total


# print(simple_multiplier(data))
print(run_dos(data))
