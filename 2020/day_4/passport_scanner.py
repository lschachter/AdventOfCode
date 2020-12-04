import re

def parse_passports():
    passports_file = open('2020/day_4/passports.text', 'r')
    passports = passports_file.read().split('\n\n')

    passports_file.close()

    return passports

def validate_passports1():
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    passports = parse_passports()
    passports = map(lambda passport: re.split('\n| ', passport), passports)

    passports_data = []

    for passport in passports:
        pass_dict = {}
        for field in passport:
            key, value = field.split(':')
            pass_dict[key] = value

        passports_data.append(pass_dict)

    valid_passports = 0

    for passport in passports_data:
        keys = set(passport.keys())
        valid_passports += 1 if required_fields.issubset(keys) else 0

    return valid_passports


#print(validate_passports1())

def validate_passports():
    rules = {
        'byr': {'length': 4, 'range': range(1920, 2003),},
        'iyr': {'length': 4, 'range': range(2010, 2021),},
        'eyr': {'length': 4, 'range': range(2020, 2031)},
        'hgt': {'cm': range(150, 194), 'in': range(59, 77)},
        'hcl': {'length': 7, 'valid': '0123456789abcdefg'},
        'ecl': {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': {'length': 9}
    }

    passports = parse_passports()
    passports = map(lambda passport: re.split('\n| ', passport), passports)

    passports_data = []

    for passport in passports:
        pass_dict = {}
        for field in passport:
            key, value = field.split(':')
            pass_dict[key] = value

        passports_data.append(pass_dict)

    valid_passports = 0

    for passport in passports_data:
        keys = set(passport.keys())

        if not set(rules.keys()).issubset(keys):
            continue

        if passport['ecl'] not in rules['ecl']:
            continue

        height = passport['hgt']
        if height[-2:] not in ['in', 'cm']:
            continue

        height_val = int(height[:-2])
        unit = height[-2:]
        if height_val not in rules['hgt'][unit]:
            continue

        hair_color = passport['hcl']
        if hair_color[0] != '#':
            continue

        hair_color = hair_color[1:]

        is_valid = True

        for ch in hair_color:
            if ch not in rules['hcl']['valid']:
                is_valid = False
                break

        length_rules = ['byr', 'iyr', 'eyr', 'pid', 'hcl']
        for field in length_rules:
            is_valid = False if len(passport[field]) != rules[field]['length'] else is_valid

            if field not in {'pid', 'hcl'} and int(passport[field]) not in rules[field]['range']:
                is_valid = False

        valid_passports += 1 if is_valid else 0

    return valid_passports

print(validate_passports())
