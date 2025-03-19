# This problem is complex, and uses the recursive backtracking algorithm.
# Examples are inside of the extras folder.
def main():
	digits = '123456789'
	target = int(input())
	solutions = []

	def backtrack(index=0, expression='', v=0):
		if index == len(digits):
			if v == target:
				solutions.append(expression)
			return

		for i in range(index, len(digits)):
			number = digits[index : i + 1]
			if index == 0:
				backtrack(i + 1, number, int(number))
			else:
				backtrack(i + 1, expression + '+' + number, v + int(number))
				backtrack(i + 1, expression + '-' + number, v - int(number))

	backtrack()
	for sol in solutions:
		print(sol)
