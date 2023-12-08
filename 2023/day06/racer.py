data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()


# ugggggggh do a binary search grossssss


def puzzle1():
    times, dists = data.split("\n")
    times = [int(x) for x in times.split(":")[1].split()]
    dists = [int(x) for x in dists.split(":")[1].split()]

    num_wins = 1
    # do binary search till you find the first option that wins
    # keep track of the farthest index that wins. once it's not better, stop
    # subtract (2 * (that index - 1)) from the (# of seconds in the race + 1)

    for i, time in enumerate(times[:]):
        maximum = time
        minimum = 0

        while maximum > (minimum + 1):
            mid = (minimum + maximum + 1) // 2
            new_dist = mid * (time - mid)
            if new_dist > dists[i]:
                maximum = mid
            else:
                minimum = mid

        num_wins *= (time + 1) - (maximum * 2)

    print(num_wins)


# puzzle1()


def puzzle2():
    time, dist = data.split("\n")
    time = int(time.split(":")[1].replace(" ", ""))
    dist = int(dist.split(":")[1].replace(" ", ""))

    maximum = time
    minimum = 0

    while maximum > (minimum + 1):
        mid = (minimum + maximum + 1) // 2
        new_dist = mid * (time - mid)
        if new_dist > dist:
            maximum = mid
        else:
            minimum = mid

    print((time + 1) - (maximum * 2))


puzzle2()
