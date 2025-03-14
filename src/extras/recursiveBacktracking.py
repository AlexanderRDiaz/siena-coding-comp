# Examples that make recursive backtracking easier to digest.

# Better fibonacci function exists inside the memoization file.
def fibonacci(n):
    if n <= 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

# A more complex example of recursive backtracking.
def getPermutations(characters):
    combinations = list()

    def backtrack(combination="", map=characters):
        if len(combination) == len(characters):
            combinations.append(combination)
            return
        for letter in map:
            tempMap = map.replace(letter, "")
            backtrack(combination + letter, tempMap)

    backtrack()
    print(combinations)
