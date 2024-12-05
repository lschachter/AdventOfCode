data_file = open("input.txt", "r")
data = data_file.read().split("\n")
data_file.close()


def report_safety():
    num_safe = 0
    for row in data:
        nums = row.split()
        nums = list(map(int, nums))

        if complex_safety(nums):
            num_safe += 1

    return num_safe


def complex_safety(nums):
    is_safe = simple_safety(nums)

    if not is_safe:
        for i in range(len(nums)):
            if simple_safety(nums[:i] + nums[i + 1 :]):
                return True

    return is_safe


def simple_safety(nums):
    current = nums[0]
    direction = 1 if nums[1] - current > 0 else -1
    is_safe = True
    for num in nums[1:]:
        if not (3 >= abs(num - current) > 0):
            is_safe = False
            break
        if num - current > 0 and direction == -1:
            is_safe = False
            break
        if num - current < 0 and direction == 1:
            is_safe = False
            break
        current = num

    return is_safe


print(report_safety())
