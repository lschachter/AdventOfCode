def parse_input_file():
    input_file = open('2020/day_8/input.txt', 'r')
    data = input_file.read().split('\n')
    input_file.close()

    return data

def get_game_data(data):
    ops = []
    for line in data:
        op, num = line.split(' ')
        ops.append([op, int(num)])

    hits = [0] * len(ops)

    return ops, hits

def run_game_loop(ops, hits):
    num_ops = len(ops)
    total = 0
    i = 0

    while i < num_ops:
        hits[i] += 1

        op, num = ops[i]
        i += 1 if op in ['acc', 'nop'] else num

        if hits[i] >= 1:
            return total

        total += num if op == 'acc' else 0

    return total

def run_game_loop2(ops, num_ops):
    i = total = 0
    hits = [0] * num_ops

    while i < num_ops:
        hits[i] += 1
        if hits[i] > 1:
            return total, False

        op, num = ops[i]
        i += 1 if op in ['acc', 'nop'] else num
        total += num if op == 'acc' else 0

    return total, True

def swap_op(change_i, ops, num_ops):
    if change_i is not None:
        ops[change_i][0] = 'jmp' if ops[change_i][0] == 'nop' else 'nop'
        change_i += 1
    else:
        change_i = 0

    for i in range(change_i, num_ops):
        if ops[i][0] in ['jmp', 'nop']:
            ops[i][0] = 'jmp' if ops[i][0] == 'nop' else 'nop'
            return i

def parse_input():
    data = parse_input_file()
    ops, _ = get_game_data(data)

    total, is_complete = 0, False
    change_i = None
    num_ops = len(ops)

    while is_complete is False:
        total, is_complete = run_game_loop2(ops, num_ops)
        if is_complete == False:
            change_i = swap_op(change_i, ops, num_ops)


    return total

print(parse_input())