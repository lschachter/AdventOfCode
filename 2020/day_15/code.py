def parse_input_file():
    input_file = open('2020/day_15/input.txt', 'r')
    data = input_file.read().split(',')
    data = list(map(int, data))

    input_file.close()

    return data

def game(num_rounds):
    starting_nums = parse_input_file()

    num_starting_nums = len(starting_nums)
    num_ages = {starting_nums[i]: i + 1 for i in range(num_starting_nums - 1)}
    last = starting_nums[-1]

    for i in range(num_starting_nums, num_rounds):
        if last not in num_ages:
            num_ages[last] = i
            last = 0
        else:
            temp = i - num_ages[last]
            num_ages[last] = i
            last = temp

    return last

print(game(2020))
print(game(30000000))
