# This problem is complex, and uses the recursive backtracking algorithm.
def main():
    digits = "123456789"
    target = int(input())
    solutions = list()

    def backtrack(index=0, expression="", v=0):
        if index == len(digits):
            if v == target:
                solutions.append(expression)
            return

        for i in range(index, len(digits)):
            number = digits[index : i + 1]
            if index == 0:
                backtrack(i + 1, number, int(number))
            else:
                backtrack(i + 1, expression + "+" + number, v + int(number))
                backtrack(i + 1, expression + "-" + number, v - int(number))

    backtrack()
    for sol in solutions:
        print(sol)

# Easier to digest example of a recursive backtracking algorithm.
def recursiveBacktrackingExample():
    digits = "abc"
    combinations = list()

    def backtrack(combination="", map=digits):
        if len(combination) == len(digits):
            combinations.append(combination)
            return
        for letter in map:
            tempMap = map.replace(letter, "")
            backtrack(combination + letter, tempMap)

    backtrack()
    print(combinations)
