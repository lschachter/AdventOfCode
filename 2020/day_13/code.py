def parse_input_file():
    input_file = open('2020/day_13/input.txt', 'r')
    data = input_file.read().split('\n')

    arrival = int(data[0])
    buses = data[1].split(',')
    input_file.close()

    return arrival, buses

def estimate_departure():
    arrival, buses = parse_input_file()
    buses = [int(bus) for bus in buses if bus != 'x']

    waits = {(bus - (arrival % bus)): bus for bus in buses}
    wait = min(waits)

    return (wait * waits[wait])

def align_departures():
    _, buses = parse_input_file()
    buses = [(int(bus), i) for i, bus in enumerate(buses) if bus != 'x']
    step = buses[0][0]
    time_stamp = 0

    for bus, i in buses[1:]:
        while (time_stamp + i) % bus != 0:
            time_stamp += step
        step *= bus

    return time_stamp


print(estimate_departure())
print(align_departures())
