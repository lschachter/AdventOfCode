import re


def parse_passports():
    passports_file = open('2020/day_4/passports.text', 'r')
    passports = passports_file.read().split('\n\n')

    passports_file.close()

    return passports

def validate_passports(validate):
    passports = parse_passports()
    passport_data = map(lambda passport: re.split('\n| ', passport), passports)

    passports = []

    for passport in passport_data:
        pass_dict = {}
        for field in passport:
            key, value = field.split(':')
            pass_dict[key] = value

        passports.append(pass_dict)

    valid_passports = 0

    for passport in passports:
        valid_passports += 1 if validate(passport) else 0

    return valid_passports

def validate_field_existence(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    return True if required_fields.issubset(set(passport.keys())) else False

def validate_passport(passport):
    rules = {
        'byr': {'length': 4, 'range': range(1920, 2003),},
        'iyr': {'length': 4, 'range': range(2010, 2021),},
        'eyr': {'length': 4, 'range': range(2020, 2031)},
        'hgt': {'cm': range(150, 194), 'in': range(59, 77)},
        'hcl': {'length': 7, 'valid': '0123456789abcdefg'},
        'ecl': {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': {'length': 9}
    }

    if not validate_field_existence(passport):
        return False

    if passport['ecl'] not in rules['ecl']:
        return False

    if passport['hgt'][-2:] not in ['in', 'cm']:
        return False

    height_val = int(passport['hgt'][:-2])
    unit = passport['hgt'][-2:]
    if height_val not in rules['hgt'][unit]:
        return False

    if passport['hcl'][0] != '#':
        return False

    for ch in passport['hcl'][1:]:
        if ch not in rules['hcl']['valid']:
            return False

    length_rules = ['byr', 'iyr', 'eyr', 'pid', 'hcl']
    for field in length_rules:
        if len(passport[field]) != rules[field]['length']:
            return False

        if field not in {'pid', 'hcl'} and int(passport[field]) not in rules[field]['range']:
            return False

    return True

print(validate_passports(validate_passport))
