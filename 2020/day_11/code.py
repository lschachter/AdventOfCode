FLOOR = '.'
OCCUPIED = '#'
OPEN = 'L'


def parse_input_file():
    input_file = open('2020/day_11/input.txt', 'r')
    data = input_file.read().split('\n')

    data = [[ch for ch in line] for line in data]
    input_file.close()

    return data

def model_seating(needs_swap):
    data = parse_input_file()
    next_round = [line.copy() for line in data]

    next_round, data = run_round(data, next_round, needs_swap)
    while data != next_round:
        next_round, data = run_round(data, next_round, needs_swap)

    return count_occupied(data)


def run_round(data, next_round, needs_swap):
    num_rows, num_cols = len(data), len(data[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if data[i][j] == FLOOR:
                continue

            if needs_swap(data, num_rows, num_cols, i, j):
                next_round[i][j] = OPEN if data[i][j] == OCCUPIED else OCCUPIED
            else:
                next_round[i][j] = data[i][j]

    return data, next_round


def needs_swap_model(data, num_rows, num_cols, i, j):
    checks = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (1, -1)]
    is_open = data[i][j] == OPEN

    num_occupied = 0
    for x, y in checks:
        check_x, check_y = x + i, y + j
        if 0 <= check_x < num_rows and 0 <= check_y < num_cols and data[check_x][check_y] == OCCUPIED:
            num_occupied += 1
            if is_open:
                return False

    return False if (not is_open and num_occupied < 4) else True

def needs_swap_real(data, num_rows, num_cols, i, j):
    checks = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (1, -1)]
    is_open = data[i][j] == OPEN

    num_occupied = 0
    for x, y in checks:
        check_x, check_y = x + i, y + j
        while 0 <= check_x < num_rows and 0 <= check_y < num_cols and data[check_x][check_y] == FLOOR:
            check_x, check_y = x + check_x, y + check_y

        if 0 <= check_x < num_rows and 0 <= check_y < num_cols and data[check_x][check_y] == OCCUPIED:
            num_occupied += 1
            if is_open:
                return False

    return False if (not is_open and num_occupied < 5) else True


def count_occupied(data):
    total = 0

    for i in range(len(data)):
        for seat in data[i]:
            total += 1 if seat == OCCUPIED else 0

    return total


print(model_seating(needs_swap_real))
