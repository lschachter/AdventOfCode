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
    rule_strings = []
    passwords = []
    for tup in password_data:
        rule, password = tup.split(': ')
        rule_strings.append(rule)
        passwords.append(password)

    password_data_file.close()

    rules = []
    Rule = collections.namedtuple('Rule', 'ch min_val max_val')

    for rule_string in rule_strings:
        ch = rule_string[-1]
        # grosssssssssssssss
        min_val, max_val = map(int, rule_string[:-1].split('-'))
        rule = Rule(ch, min_val, max_val)
        rules.append(rule)

    return rules, passwords


def validate_passwords(validator):
    rules, passwords = parse_passwords()
    valid = 0

    num_passwords = len(passwords)
    for i in range(num_passwords):
        if validator(rules[i], passwords[i]):
            valid += 1

    return valid

def is_sled_valid(rule, password):
    if rule.min_val <= password.count(rule.ch) <= rule.max_val:
        return True

    return False

def is_toboggan_valid(rule, password):
    if (
        (password[rule.min_val - 1] != rule.ch and password[rule.max_val - 1] == rule.ch)
        or (password[rule.min_val - 1] == rule.ch and password[rule.max_val - 1] != rule.ch)
    ):
        return True

    return False


print(validate_passwords(is_sled_valid))
print(validate_passwords(is_toboggan_valid))
