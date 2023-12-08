data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()

from collections import defaultdict


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.order = "TJQKA"
        self.type = self.find_type()

    def get_frequencies(self):
        self.freqs_dict = defaultdict(int)
        for card in self.hand:
            self.freqs_dict[card] += 1

        freqs = list(self.freqs_dict.items())
        freqs.sort(key=lambda pair: pair[1], reverse=True)

        return freqs

    def find_type(self):
        freqs = self.get_frequencies()

        if freqs[0][1] >= 4:
            return freqs[0][1] + 2
        if freqs[0][1] == 3 and freqs[1][1] == 2:
            return 5
        if freqs[0][1] == 3:
            return 4
        if freqs[0][1] == 2 and freqs[1][1] == 2:
            return 3
        if freqs[0][1] == 2:
            return 2
        return 1

    def __gt__(self, other):
        for i, card in enumerate(self.hand):
            if card == other.hand[i]:
                continue
            if other.hand[i] in self.order and card in self.order:
                return self.order.index(card) > self.order.index(other.hand[i])
            if card in self.order:
                return True
            if other.hand[i] in self.order:
                return False
            return card > other.hand[i]

        return False

    def __str__(self):
        return f"{self.hand}: {self.bid}, {self.type}"


class Hand2(Hand):
    def __init__(self, hand, bid):
        super().__init__(hand, bid)
        self.type = self.find_type()
        self.order = "J23456789TQKA"

    def find_type(self):
        freqs = self.get_frequencies()

        if "J" not in self.freqs_dict or self.freqs_dict["J"] == 5:
            return super().find_type()

        j_count = self.freqs_dict["J"]

        if len(freqs) == 2:
            return 7
        if (freqs[0][1] + j_count == 4 and freqs[0][0] != "J") or (
            freqs[1][1] + j_count == 4 and freqs[1][0] != "J"
        ):
            return 6
        if (freqs[0][1] + j_count) == 3 and freqs[1][1] == 2:
            return 5
        if j_count == 2 and freqs[1][1] == 1 or freqs[0][1] == 2 and j_count == 1:
            return 4
        if freqs[0][1] == 2 and j_count == 1 or j_count == 2:
            return 3
        return 2


def puzzle1():
    hands = [
        Hand(hand, int(bid))
        for hand, bid in map(lambda pair: pair.split(), data.split("\n"))
    ]

    hands.sort(key=lambda hand: (hand.type, hand))

    winnings = 0

    for i, hand in enumerate(hands):
        winnings += (i + 1) * hand.bid

    print(winnings)


# puzzle1()


def puzzle2():
    hands = [
        Hand2(hand, int(bid))
        for hand, bid in map(lambda pair: pair.split(), data.split("\n"))
    ]

    hands.sort(key=lambda hand: (hand.type, hand))

    # for hand in hands:
    #     print(hand)

    winnings = 0

    for i, hand in enumerate(hands):
        winnings += (i + 1) * hand.bid

    print(winnings)


puzzle2()
