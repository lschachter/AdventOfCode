
def run_intcode(intcode_file):
    start_code = open(intcode_file, 'r').read().split(',')
    start_code = list(map(int, start_code))
    len_intcode = len(start_code)
    target = 19690720
    
    for noun in range(99):
        for verb in range(99):
            intcode = start_code.copy()
            intcode[1] = noun
            intcode[2] = verb
            run_instructions(intcode, len_intcode)
            if intcode[0] == target:
                return 100 * noun + verb
    
    return None

def run_instructions(intcode, len_intcode):
    for i in range(0, len_intcode, 4):
        if intcode[i] == 99:
            break
        i1 = intcode[i + 1]
        i2 = intcode[i + 2]
        i3 = intcode[i + 3]
        if intcode[i] == 1:
            intcode[i3] = intcode[i1] + intcode[i2]
        elif intcode[i] == 2:
            intcode[i3] = intcode[i1] * intcode[i2]
        else:
            break

print(run_intcode("intcode.txt"))
