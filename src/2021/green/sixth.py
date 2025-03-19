# This problem is complex, and uses tree traversal & recursion.
# Examples are inside of the extras folder.
def solution():
    digits = '123456789'
    target = int(input())
    solutions = []

    def evalExpression(expression, index=0):
        if expression.find('_') == -1:
            if eval(expression) == target:
                solutions.append(expression)
            return

        for i in range(index, len(expression)):
            if expression[i] != '_':
                continue

            evalExpression(expression[:i] + '+' + expression[i + 1 :], i + 1)
            evalExpression(expression[:i] + '-' + expression[i + 1 :], i + 1)

    def genExpression(index=0, expression=''):
        if index == len(digits):
            evalExpression(expression)

        for i in range(index, len(digits)):
            number = digits[index : i + 1]
            if index == 0:
                genExpression(i + 1, number)
            else:
                genExpression(i + 1, expression + '_' + number)

    genExpression()

    if len(solutions) == 0:
        print('NO SOLUTIONS FOUND')
    else:
        for sol in solutions:
            print(sol)
