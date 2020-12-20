import operator

OPS = {'+' : operator.add, '*' : operator.mul}

def parse_input_file():
    input_file = open('2020/day_18/input.txt', 'r')
    data = input_file.read().split('\n')
    input_file.close()

    return data

def solve_math(solve):
    data = parse_input_file()

    stacks = [evaluate(expression, solve) for expression in data]

    return(sum(stacks))

# Assumes each expression is valid
def evaluate(expression, solve):
    expression = [ch for ch in expression if ch != ' ']
    stack = []

    while len(expression) > 0:
        if expression[0] != ')':
            stack.append(expression.pop(0))
        else:
            expression.pop(0)
            internal = stack.pop(-1)
            current = []
            while internal != '(':
                current.append(internal)
                internal = stack.pop(-1)
            stack.append(solve(current))

    stack.reverse()
    return solve(stack)

def solve_internal_expression_simple(expression):
    while len(expression) > 1:
        num2, op, num1 = expression.pop(-1), expression.pop(-1), expression.pop(-1)
        expression.append(OPS[op](int(num1), int(num2)))

    return expression[0]

def solve_internal_expression_advanced(expression):
    # Sweep for addition
    addition_complete = False

    while not addition_complete:
        original = expression
        for i in range(len(expression)):
            if expression[i] == '+':
                num2, op, num1 = expression[i - 1], expression[i], expression[i + 1]
                addition = OPS[op](int(num1), int(num2))
                expression = expression[:i - 1] + [addition] + expression[i + 2:]
                break
        if original == expression:
            addition_complete = True

    return solve_internal_expression_simple(expression)


print(solve_math(solve_internal_expression_simple))
print(solve_math(solve_internal_expression_advanced))
