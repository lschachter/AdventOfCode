'''
ok so again, i think we should sort each password. then since each rule only has one letter,
we can go through till we find that letter and count how many there are but as i write this
i remember python has a string.count() function so lol fuck that

i guess it's just a matter of correctly parsing the numbers in the rule and then checking that
min_ch <= password.count(valid_ch) <= max_ch cool let's go with that
'''

import collections


def parse_passwords():
    password_data_file = open('2020/day_2/passwords.text', 'r')
    password_data = password_data_file.read().split('\n')

    Rule = collections.namedtuple('Rule', 'ch min_val max_val password')
    rules = []

    for line in password_data:
        vals, ch, password = line.split()
        ch = ch[0]
        min_val, max_val = map(int, vals.split('-'))
        rules.append(Rule(ch, min_val, max_val, password))

    password_data_file.close()
    return rules


def validate_passwords(validate):
    rules = parse_passwords()
    valid = 0

    for rule in rules:
        valid += 1 if validate(rule, rule.password) else 0

    return valid


def is_sled_valid(rule, password):
    return True if rule.min_val <= password.count(rule.ch) <= rule.max_val else False


def is_toboggan_valid(rule, password):
    if (
        (password[rule.min_val - 1] != rule.ch and password[rule.max_val - 1] == rule.ch)
        or (password[rule.min_val - 1] == rule.ch and password[rule.max_val - 1] != rule.ch)
    ):
        return True

    return False


print(validate_passwords(is_sled_valid))
print(validate_passwords(is_toboggan_valid))
