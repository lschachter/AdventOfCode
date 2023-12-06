data_file = open("input.txt", "r")
data = data_file.read().split("\n")
data_file.close()


def puzzle1():
    sum_engine_ids = 0
    symbols = "~!@#$%^&*()_+`-=\][|}{;:'\"}],/<>?"

    x_len = len(data[0])
    for i, line in enumerate(data):
        p1 = 0
        num_str = ""
        while p1 < x_len:
            if not line[p1].isnumeric():
                p1 += 1
                continue

            while p1 < x_len and line[p1].isnumeric():
                num_str += line[p1]
                p1 += 1

            if num_str:
                min_x = p1 - len(num_str) - 1

                is_valid = False

                for x in range(min_x, min(p1 + 1, x_len)):
                    for y in range(i - 1, min(i + 2, len(data))):
                        if data[y][x] in symbols:
                            is_valid = True
                            break
                    if is_valid:
                        sum_engine_ids += int(num_str)
                        is_valid = False
                        break

                num_str = ""

    print(sum_engine_ids)


# puzzle1()


def puzzle2():
    sum_gear_ratios = 0

    x_len = len(data[0])
    for i, line in enumerate(data):
        gear_ratio_strs = []
        p1 = 0

        while p1 < x_len:
            if line[p1] != "*":
                p1 += 1
                continue

            num_str = ""
            checked_x = p1 - 1
            for y in range(i - 1, min(i + 2, len(data))):
                for x in range(p1 - 1, min(p1 + 2, x_len)):
                    if checked_x > x:
                        continue
                    if data[y][x].isnumeric():
                        # get to front of number
                        new_x = x
                        while new_x >= 0 and data[y][new_x].isnumeric():
                            num_str = data[y][new_x] + num_str
                            new_x -= 1
                        new_x = x + 1
                        while new_x < x_len and data[y][new_x].isnumeric():
                            num_str += data[y][new_x]
                            new_x += 1

                        checked_x = new_x + 1

                        gear_ratio_strs.append(num_str)
                        num_str = ""
                checked_x = 0

            if len(gear_ratio_strs) == 2:
                sum_gear_ratios += int(gear_ratio_strs[0]) * int(gear_ratio_strs[1])

            gear_ratio_strs = []
            p1 += 1

    print(sum_gear_ratios)


puzzle2()
