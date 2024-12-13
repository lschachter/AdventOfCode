import time

data_file = open("input.txt", "r")
data = data_file.read()
data = list(map(int, data.split()))
data_file.close()

evolutions = 25


def evolve_stone():
    time_start = time.time()
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

    time_end = time.time()
    print(time_end - time_start)

    return len(output)


print(evolve_stone())


"""
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


output = data
    num_stones = len(output)
    for _ in range(evolutions):
        original = output[:num_stones]
        output = [None] * len(original)
        num_stones = 0

        for stone in original:
            if num_stones >= len(output) - 3:
                output += [None] * len(original)
            if stone == 0:
                output[num_stones] = 1
                num_stones += 1
                continue
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                output[num_stones] = int(stone_str[: len(stone_str) // 2])
                num_stones += 1
                output[num_stones] = int(stone_str[len(stone_str) // 2 :])
                num_stones += 1
            else:
                output[num_stones] = stone * 2024
                num_stones += 1
"""
