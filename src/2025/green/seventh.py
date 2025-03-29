""""""

"""A'BC'D+A'B'C'D'+A'B'CD'+A'BCD+ABD+AB'D'"""
"""BD+B'D'"""
""" -> equivalent"""
expr1, expr2 = input(), input()


def addAnds(expression):
    i = 1
    while i < len(expression):
        prev, cur = expression[i - 1], expression[i]
        if prev == "'":
            prev = expression[i - 2]

        if cur in 'ABCD' and prev in 'ABCD':
            expression = expression[:i] + ' and ' + expression[i:]
            i += 5
        i += 1
    return expression


def convertOrs(expression):
    i = 1
    while i < len(expression):
        if expression[i] == '+':
            expression = expression[:i] + ' or ' + expression[i + 1 :]
            i += 4
        i += 1
    return expression


def convertNots(expression):
    i = 1
    while i < len(expression):
        if expression[i] == "'":
            if i < 2:
                expression = 'not ' + expression[i - 1] + expression[i + 1 :]
            else:
                expression = expression[: i - 1] + 'not ' + expression[i - 1] + expression[i + 1 :]
            i += 4
        i += 1
    return expression


expr1 = convertNots(convertOrs(addAnds(expr1)))
expr2 = convertNots(convertOrs(addAnds(expr2)))
values = [True, False]

valid = True
for A in values:  # noqa
    for B in values:  # noqa
        for C in values:  # noqa
            for D in values:  # noqa
                if eval(expr1) != eval(expr2):
                    valid = False

if valid:
    print('EQUIVALENT')
else:
    print('NOT EQUIVALENT')
