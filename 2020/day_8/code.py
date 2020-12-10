def parse_input_file():
    input_file = open('2020/day_8/input.txt', 'r')
    data = input_file.read().split('\n')
    input_file.close()

    return data

def get_game_ops(data):
    ops = []
    for line in data:
        op, num = line.split(' ')
        ops.append([op, int(num)])

    return ops

def run_game_loop(ops, num_ops):
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

def swap_next_op(change_i, ops):
    if change_i is not None:
        ops[change_i][0] = 'jmp' if ops[change_i][0] == 'nop' else 'nop'
        change_i += 1
    else:
        change_i = 0

    while ops[change_i][0] not in ['jmp', 'nop']:
        change_i += 1

    ops[change_i][0] = 'jmp' if ops[change_i][0] == 'nop' else 'nop'

    return change_i

def parse_input(game_runner):
    data = parse_input_file()
    ops = get_game_ops(data)

    num_ops = len(ops)

    return game_runner(ops, num_ops)

def run_until_break(ops, num_ops):
    return run_game_loop(ops, num_ops)[0]

def run_full_game(ops, num_ops):
    is_complete = False
    change_i = None

    while is_complete is False:
        total, is_complete = run_game_loop(ops, num_ops)
        change_i = swap_next_op(change_i, ops) if is_complete == False else change_i

    return total

print(parse_input(run_until_break))
print(parse_input(run_full_game))
