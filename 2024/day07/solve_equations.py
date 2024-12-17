data_file = open("input.txt", "r")
data = data_file.read().splitlines()

data_file.close()


def build_equations():
    equations = list(map(lambda eq: eq.split(": "), data))

    for eq in equations:
        eq[0] = int(eq[0])
        eq[1] = list(map(int, eq[1].split()))

    return equations


def check_equations():
    equations = build_equations()
    total = 0

    for answer, nums in equations:
        if check_equation(answer, nums[1:], nums[0]):

            total += answer

    return total


def check_equation(answer, nums, check):
    if not nums:
        return check == answer

    return check_equation(answer, nums[1:], check + nums[0]) or check_equation(
        answer, nums[1:], check * nums[0]
    )


print(check_equations())
