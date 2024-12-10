data_file = open("input.txt", "r")
data = list(map(int, data_file.read()))
data_file.close()


def map_space():
    output = []

    for i in range(len(data)):
        if i % 2 == 0:  # it's a file
            output += [i // 2] * data[i]  # for _ in range(data[i])
        else:  # it's open space
            # let's just do it separately for now cuz we're confusing ourselves optimizing
            output += ["."] * data[i]

    return output


def flatten_by_chunk():
    output = map_space()

    p2 = len(output) - 1

    for _ in range(len(data) // 2):
        current_id = output[p2]
        space_needed = count_space_needed(output, current_id, p2)
        i = 0

        while i < p2:
            space_found = 0
            while i < p2 and output[i] == ".":
                space_found += 1
                i += 1

            if space_found >= space_needed:
                for j in range(space_needed):
                    output[i - space_found + j], output[p2] = (
                        output[p2],
                        output[i - space_found + j],
                    )
                    p2 -= 1

                break

            i += 1
        if current_id == output[p2]:  # if the placement failed, skip it
            p2 -= space_needed
        while output[p2] == ".":
            p2 -= 1

    checksum = 0
    for i, num in enumerate(output):
        if num == ".":
            continue

        checksum += i * num

    return checksum


def count_space_needed(output, current_id, p2):
    space_needed = 0

    while p2 >= 0 and output[p2] == current_id:
        space_needed += 1
        p2 -= 1

    return space_needed


def flatten_individually():
    output = map_space()
    i = 0
    p2 = len(output) - 1

    while i < p2:
        if output[i] == ".":
            output[i], output[p2] = output[p2], output[i]
            p2 -= 1
            while output[p2] == ".":
                p2 -= 1
        i += 1

    checksum = 0
    for i, num in enumerate(output):
        if num == ".":
            break

        checksum += i * num

    return checksum


print(flatten_by_chunk())
