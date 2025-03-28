def evalExpression(expression: str, solutions: list[str], target: int, index: int = 0) -> None:
    if expression.find('_') == -1:
        if eval(expression) == target:
            solutions.append(expression)
        return

    for i in range(index, len(expression)):
        if expression[i] != '_':
            continue

        evalExpression(expression[:i] + '+' + expression[i + 1 :], solutions, target, i + 1)
        evalExpression(expression[:i] + '-' + expression[i + 1 :], solutions, target, i + 1)


def createExpressions(
    expressions,
    expression: str = '',
    digits: str = '123456789',
    index: int = 0,
) -> None:
    if index == len(digits):
        expressions.append(expression)

    for i in range(index, len(digits)):
        number = digits[index : i + 1]
        if index == 0:
            createExpressions(i + 1, number)
        else:
            createExpressions(i + 1, expression + '_' + number)


def getExpressions(target: int) -> list[str]:
    target = int(input())

    expressions = []
    solutions = []

    createExpressions(expressions)
    for expression in expressions:
        evalExpression(expression, solutions, target)

    if len(solutions) == 0:
        return ['NO SOLUTIONS FOUND']
    else:
        return solutions


if __name__ == '__main__':
    target = int(input())
    result = getExpressions(target)
    for string in result:
        print(string)
