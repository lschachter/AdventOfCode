from multiprocessing import Pool

data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()

towels, designs = data.split("\n\n")
towels = towels.split(", ")
designs = designs.split("\n")


def find_possible_towels():
    def build_towel(goal, current=""):
        if current == goal:
            return True

        for towel in towels:
            if towel != goal[len(current) : len(current) + len(towel)]:
                continue

            if build_towel(goal, current + towel):
                return True

        return False

    num_possible = 0
    for design in designs:
        starts = [towel for towel in towels if design.startswith(towel)]

        for towel in starts:
            if build_towel(design, towel):
                num_possible += 1
                break

    return num_possible


# print(find_possible_towels())


def find_towel_iterations():
    # TOO SLOW, DOES NOT WORK
    global build_towel

    def build_towel(goal, num_versions=0, current=""):
        if current == goal:
            return num_versions + 1

        for towel in towels:
            if towel != goal[len(current) : len(current) + len(towel)]:
                continue

            num_versions = build_towel(goal, num_versions, current + towel)

        return num_versions

    num_possible = 0
    for design in designs:
        num_possible += build_towel(design, 0)
    return num_possible

    # return num_possible
    # if __name__ == "__main__":
    #     pool = Pool(processes=len(designs))
    #     outputs = pool.map(build_towel, designs)

    #     print(sum(outputs))


print(find_towel_iterations())
