data_file = open("input.txt", "r")
data = data_file.read().split("\n")
data_file.close()


def puzzle1():
    total_points = 0
    for card in data:
        winners, numbers = card.split(" | ")
        winners = winners.split(": ")[1]

        winners = set(map(lambda x: int(x), winners.split()))
        numbers = list(map(lambda x: int(x), numbers.split()))

        points = 0

        for num in numbers:
            if num in winners:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        total_points += points

    print(total_points)


# puzzle1()


def puzzle2():
    num_cards = {i: 1 for i in range(len(data))}

    for id, card in enumerate(data):
        winners, numbers = card.split(" | ")
        winners = winners.split(": ")[1]

        winners = set(map(lambda x: int(x), winners.split()))
        numbers = list(map(lambda x: int(x), numbers.split()))

        num_copies = 0
        for num in numbers:
            if num in winners:
                num_copies += 1

        for i in range(id + 1, id + 1 + num_copies):
            num_cards[i] += num_cards[id]

    print(sum(num_cards.values()))


puzzle2()
