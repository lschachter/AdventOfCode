data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()


def puzzle1():
    global handle_history

    histories = [[int(x) for x in history.split()] for history in data.split("\n")]

    def handle_history(history):
        differences = [history]

        while not all(diff == 0 for diff in differences[-1]):
            differences.append(
                [
                    differences[-1][i] - differences[-1][i - 1]
                    for i in range(1, len(differences[-1]))
                ]
            )

        ans = 0
        for diff in differences:
            ans += diff[-1]

        return ans

    if __name__ == "__main__":
        import multiprocessing

        pool = multiprocessing.Pool(processes=len(histories))
        print(sum(pool.map(handle_history, histories)))


# puzzle1()


def puzzle2():
    global handle_history

    histories = [[int(x) for x in history.split()] for history in data.split("\n")]

    def handle_history(history):
        differences = [history]

        while not all(diff == 0 for diff in differences[-1]):
            differences.append(
                [
                    differences[-1][i] - differences[-1][i - 1]
                    for i in range(1, len(differences[-1]))
                ]
            )

        ans = 0
        for i in range(len(differences) - 2, -1, -1):
            ans = differences[i][0] - ans

        return ans

    if __name__ == "__main__":
        import multiprocessing

        pool = multiprocessing.Pool(processes=len(histories))
        print(sum(pool.map(handle_history, histories)))


puzzle2()
