def parse_input_file():
    input_file = open('2020/day_5/input.txt', 'r')
    data = input_file.read().split('\n')

    input_file.close()

    return data

def scan_seats():
    seat_strings = parse_input_file()

    row_min, row_max = 0, 127
    col_min, col_max = 0, 7
    row_up, col_up = 'B', 'R'

    seats = {}

    for seat in seat_strings:
        row = binary_search(row_up, seat[:7], row_min, row_max)
        col = binary_search(col_up, seat[7:], col_min, col_max)
        seats[seat] = {'row': row, 'col': col}
        seats[seat]['id'] = (seats[seat]['row'] * 8) + col

    ids = [seats[seat]['id'] for seat in seats]
    # return max(ids)
    ids.sort()

    for i in range(1, len(ids)):
        if ids[i - 1] == ids[i] - 2:
            return ids[i] - 1

def binary_search(up, instructions, minimum, maximum):
    if len(instructions) == 0:
        return minimum

    mid = (minimum + maximum + 1) // 2
    if instructions[0] == up:
        minimum = mid
    else:
        maximum = mid
    return binary_search(up, instructions[1:], minimum, maximum)


print(scan_seats())
