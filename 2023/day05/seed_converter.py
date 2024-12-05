data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()


def puzzle1():
    maps = data.split("\n\n")
    seeds = map(lambda seed: int(seed), maps.pop(0).split(": ")[1].split())

    maps = dict(map(lambda item: item.split(" map:\n"), maps))

    for name in maps:
        maps[name] = list(
            map(lambda string: string.split(), maps[name].split("\n")),
        )

    for name in maps:
        for i, section in enumerate(maps[name]):
            maps[name][i] = [
                range(int(section[1]), int(section[1]) + int(section[2]) + 1),
                range(int(section[0]), int(section[0]) + int(section[2]) + 1),
            ]

    min_location = float("inf")

    for converter in seeds:
        for ranges in maps.values():
            for section in ranges:
                if converter in section[0]:
                    diff = converter - section[0].start
                    converter = section[1].start + diff
                    break

        min_location = min(min_location, converter)

    print(min_location)


# puzzle1()


def puzzle2():
    maps = data.split("\n\n")
    seeds = list(map(lambda seed: int(seed), maps.pop(0).split(": ")[1].split()))

    seed_ranges = []

    for i in range(0, len(seeds) - 1, 2):
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))

    maps = dict(map(lambda item: item.split(" map:\n"), maps))

    for name in maps:
        maps[name] = list(
            map(lambda string: string.split(), maps[name].split("\n")),
        )

    for name in maps:
        for i, section in enumerate(maps[name]):
            maps[name][i] = [
                range(int(section[1]), int(section[1]) + int(section[2]) + 1),
                range(int(section[0]), int(section[0]) + int(section[2]) + 1),
            ]

    # found_conversions = {name: {} for name in maps}

    min_location = float("inf")
    for seed_range in seed_ranges:
        for converter in seed_range:
            for ranges in maps.values():
                for section in ranges:
                    if converter in section[0]:
                        diff = converter - section[0].start
                        converter = section[1].start + diff
                        break

            min_location = min(min_location, converter)

    print(min_location)
    # print(found_conversions)


# puzzle2()


# COPIED FROM https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py

# parts = data.split("\n\n")
# seed, *others = parts
# seed = [int(x) for x in seed.split(":")[1].split()]


# class Function:
#     def __init__(self, S):
#         lines = S.split("\n")[1:]  # throw away name
#         # dst src sz
#         self.tuples: list[tuple[int, int, int]] = [
#             [int(x) for x in line.split()] for line in lines
#         ]
#         # print(self.tuples)

#     def apply_one(self, x: int) -> int:
#         for dst, src, sz in self.tuples:
#             if src <= x < src + sz:
#                 return x + dst - src
#         return x

#     # list of [start, end) ranges
#     def apply_range(self, R):
#         A = []
#         for dest, src, sz in self.tuples:
#             src_end = src + sz
#             NR = []
#             while R:
#                 # [st                                     ed)
#                 #          [src       src_end]
#                 # [BEFORE ][INTER            ][AFTER        )
#                 (st, ed) = R.pop()
#                 # (src,sz) might cut (st,ed)
#                 before = (st, min(ed, src))
#                 inter = (max(st, src), min(src_end, ed))
#                 after = (max(src_end, st), ed)
#                 if before[1] > before[0]:
#                     NR.append(before)
#                 if inter[1] > inter[0]:
#                     A.append((inter[0] - src + dest, inter[1] - src + dest))
#                 if after[1] > after[0]:
#                     NR.append(after)
#             R = NR
#         return A + R


# Fs = [Function(s) for s in others]


# # def f(R, o):
# #     A = []
# #     for line in o:
# #         dest, src, sz = [int(x) for x in line.split()]
# #         src_end = src + sz


# # P1 = []
# # for x in seed:
# #     for f in Fs:
# #         x = f.apply_one(x)
# #     P1.append(x)
# # print(min(P1))

# P2 = []
# pairs = list(zip(seed[::2], seed[1::2]))
# for st, sz in pairs:
#     # inclusive on the left, exclusive on the right
#     # e.g. [1,3) = [1,2]
#     # length of [a,b) = b-a
#     # [a,b) + [b,c) = [a,c)
#     R = [(st, st + sz)]
#     for f in Fs:
#         R = f.apply_range(R)
#     # print(len(R))
#     P2.append(min(R)[0])
# print(min(P2))
