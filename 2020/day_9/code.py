def parse_input_file():
    input_file = open('2020/day_9/input.txt', 'r')
    data = list(map(int, input_file.read().split('\n')))
    input_file.close()

    return data

def decrypt_data(data, preamble_length):
    data_length = len(data)

    for i in range(preamble_length, data_length):
        if can_two_sum(data[i], data[(i - preamble_length): i]) is False:
            return i, data[i]

def can_two_sum(k, nums):
    nums = sorted(nums)

    p1 = 0
    p2 = len(nums) - 1

    while p1 != p2:
        if nums[p1] + nums[p2] == k:
            return True
        if nums[p1] + nums[p2] < k:
            p1 += 1
        else:
            p2 -= 1

    return False

def find_weakness():
    data = parse_input_file()

    index, invalid = decrypt_data(data, 25)
    start, end = sum_set(data, index, invalid)
    invalid_list = data[start: end + 1]

    return min(invalid_list) + max(invalid_list)

def sum_set(data, index, k):
    p1 = 0
    p2 = 1

    total = data[p1] + data[p2]

    # Assumes that there IS an answer
    while total != k:
        if total < k:
            p2 += 1
            total += data[p2]
        else:
            last_change = p1
            total -= data[p1]
            p1 += 1

    return last_change, p2


print(find_weakness())
