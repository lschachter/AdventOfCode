data_file = open("input.txt", "r")
data = data_file.read().split("\n")
data_file.close()


def puzzle1():
    total = 0

    for line in data:
        p1 = 0
        p2 = len(line) - 1
        while not line[p1].isnumeric():
            p1 += 1
        while not line[p2].isnumeric():
            p2 -= 1
        total += int(line[p1] + line[p2])

    print(total)


def puzzle2():
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    total = 0

    for line in data:
        num_str = ""
        p1 = 0
        p2 = len(line) - 1
        is_found = False
        while not line[p1].isnumeric() and not is_found:
            for i, num in enumerate(nums):
                if line[p1 : p1 + len(num)] == num:
                    num_str += str(i + 1)
                    is_found = True
                    break
            p1 += 1
        if not is_found:
            num_str += line[p1]

        is_found = False
        while not line[p2].isnumeric() and not is_found:
            for i, num in enumerate(nums):
                if line[p2 - len(num) + 1 : p2 + 1] == num:
                    num_str += str(i + 1)
                    is_found = True
                    break
            p2 -= 1
        if not is_found:
            num_str += line[p2]

        print(num_str)

        total += int(num_str)

    print(total)


puzzle2()
