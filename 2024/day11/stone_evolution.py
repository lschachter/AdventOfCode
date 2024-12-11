data_file = open("input.txt", "r")
data = data_file.read()
data = list(map(int, data.split()))
data_file.close()

evolutions = 75


def evolve_stone():
    output = data
    for _ in range(evolutions):
        original = output
        output = []

        for stone in original:
            if stone == 0:
                output.append(1)
                continue
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                output.append(int(stone_str[: len(stone_str) // 2]))
                output.append(int(stone_str[len(stone_str) // 2 :]))
            else:
                output.append(stone * 2024)

    return len(output)


print(evolve_stone())
