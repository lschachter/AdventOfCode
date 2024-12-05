data_file = open("input.txt", "r")
data = data_file.read()
data_file.close()

def hash(item):
    num = 0
    for ch in item:
        num += ord(ch)
        num *= 17
        num = num % 256

    return num


def puzzle1():
    sequence = data.split(",")
    total = 0
    for item in sequence:

        total += hash(item)
    print(total)


# puzzle1()

def puzzle2():
    
