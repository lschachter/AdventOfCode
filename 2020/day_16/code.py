import re

def parse_input_file():
    input_file = open('2020/day_16/input.txt', 'r')

    range_data, your_ticket, nearby_tickets = input_file.read().split('\n\n')
    range_data = range_data.split('\n')
    fields = fields_by_field(range_data)

    your_ticket = list(map(int, re.split('\n|,', your_ticket)[1:]))
    nearby_tickets = nearby_tickets.split('\n')[1:]
    nearby_tickets = [list(map(int, ticket.split(','))) for ticket in nearby_tickets]

    input_file.close()

    return fields, your_ticket, nearby_tickets

def fields_by_field(range_data):
    fields = {}
    for field in range_data:
        field, num_str = field.split(':')
        ranges_str = num_str.split(' or ')
        ranges = []
        for span in ranges_str:
            span = span.split('-')
            span = range(int(span[0]), int(span[1]) + 1)
            ranges.append(span)
        fields[field] = ranges

    return fields

def count_invalid():
    fields, your_ticket, nearby_tickets = parse_input_file()
    ranges = get_ranges(fields)

    num_invalid = 0
    for ticket in nearby_tickets:
        for num in ticket:
            is_valid = False
            for span in ranges:
                if num in span:
                    is_valid = True
                    break

            num_invalid += num if not is_valid else 0

    return num_invalid

def get_ranges(fields):
    ranges = []
    for range_set in fields.values():
        ranges.extend(range_set)

    return ranges

def validate_tickets():
    fields, your_ticket, nearby_tickets = parse_input_file()

    num_fields = len(fields)
    field_options = {field: list(range(num_fields)) for field in fields}

    ranges = get_ranges(fields)
    nearby_tickets = get_valid_tickets(nearby_tickets, ranges)

    for ticket in nearby_tickets:
        for i in range(num_fields):
            for field in fields:
                num = ticket[i]
                spans = fields[field]
                field_options[field].remove(i) if num not in spans[0] and num not in spans[1] else None

    found = {}
    while len(found) != num_fields:
        newly_found = set()
        for field in fields:
            if field in field_options and len(field_options[field]) == 1:
                found[field] = field_options.pop(field)[0]
                newly_found.add(found[field])

        for field in field_options:
            [field_options[field].remove(num) if num in field_options[field] else None for num in newly_found]

    return multiply_your_departure_data(your_ticket, found)

def get_valid_tickets(nearby_tickets, ranges):
    valid_nearby_tickets = []

    for ticket in nearby_tickets:
        is_ticket_valid = True
        for num in ticket:
            is_valid = False
            for span in ranges:
                if num in span:
                    is_valid = True
                    break

            is_ticket_valid = False if not is_valid else is_ticket_valid

        valid_nearby_tickets.append(ticket) if is_ticket_valid else None

    return valid_nearby_tickets

def multiply_your_departure_data(your_ticket, found):
    departure_data = 1
    for field in found:
        departure_data *= your_ticket[found[field]] if 'departure' in field else 1

    return departure_data


print(count_invalid())
print(validate_tickets())
