data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()


def puzzle1():
    print(
        max(
            [
                sum([int(row) for row in elf_cals.split("\n")])
                for elf_cals in data.split("\n\n")
            ]
        )
    )


# puzzle1()


def puzzle2():
    per_elf = [
        sum([int(row) for row in elf_cals.split("\n")])
        for elf_cals in data.split("\n\n")
    ]
    per_elf.sort(reverse=True)
    print(sum(per_elf[:3]))


puzzle2()
