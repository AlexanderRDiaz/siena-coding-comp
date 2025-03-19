from copy import deepcopy


def getHints():
	top = list(input().upper())

	rows = []
	for _ in range(5):
		rows.append(list(input().upper()))

	columns = []
	temp1 = top.copy()
	temp1.pop(len(top) - 1)
	temp1.pop(0)

	bottom = list(input().upper())
	temp2 = bottom.copy()
	temp2.pop(len(bottom) - 1)
	temp2.pop(0)

	for i in range(5):
		columns.append([temp1[i], temp2[i]])

	diagonal1 = (
		[0, 0],
		[1, 1],
		[2, 2],
		[3, 3],
		[4, 4],
	)

	diagonal2 = (
		[0, 4],
		[1, 3],
		[2, 2],
		[3, 1],
		[4, 0],
	)

	diagonals = {
		top[0]: diagonal1,
		top[6]: diagonal2,
		bottom[0]: diagonal2,
		bottom[6]: diagonal1,
	}

	return rows, columns, diagonals


def getNeighbors(pos):
	neighbors = [
		[pos[0] - 1, pos[1] - 1],
		[pos[0] - 1, pos[1]],
		[pos[0] - 1, pos[1] + 1],
		[pos[0], pos[1] - 1],
		[pos[0], pos[1] + 1],
		[pos[0] + 1, pos[1] - 1],
		[pos[0] + 1, pos[1]],
		[pos[0] + 1, pos[1] + 1],
	]

	i = 0
	while i < len(neighbors):
		row, column = neighbors[i][0], neighbors[i][1]

		if not (0 <= row < 5) or not (0 <= column < 5):
			neighbors.pop(i)
		else:
			i += 1

	return neighbors


def solveHints(pos, _rowHints_, _columnHints_, _diagonalHints_):
	rowNum, columnNum = pos[0], pos[1]
	rowHints, columnHints = _rowHints_[rowNum], _columnHints_[columnNum]

	diagonalHints = []
	for char, diagPoses in _diagonalHints_.items():
		for dPos in diagPoses:
			sameRow = dPos[0] == rowNum
			sameColumn = dPos[1] == columnNum
			if sameRow and sameColumn:
				diagonalHints.append(char)

	allHints = []
	allHints.extend(rowHints)
	allHints.extend(columnHints)
	allHints.extend(diagonalHints)

	return allHints


# Another complex use of recursive backtracking, examples of recursive backtracking are in extras.
def main():
	_rowHints_, _columnHints_, _diagonalHints_ = getHints()
	_puzzle_ = [['' for _ in range(5)] for _ in range(5)]

	start = [int(v) for v in input().split(' ')]
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXY'

	def backtrack(index=0, pos=start, puzzle=_puzzle_):
		if index == len(letters):
			for row in puzzle:
				print(str(row))
		elif index == 0:
			puzzle[pos[0]][pos[1]] = 'A'
			index += 1

		for neighborPosition in getNeighbors(pos):
			rowNum, columnNum = neighborPosition[0], neighborPosition[1]
			allHints = solveHints(neighborPosition, _rowHints_, _columnHints_, _diagonalHints_)
			found = letters[index] in allHints
			if (len(puzzle[rowNum][columnNum]) == 0) and found:
				newPuzzle = deepcopy(puzzle)
				newPuzzle[rowNum][columnNum] = newPuzzle[rowNum][columnNum] + letters[index]
				backtrack(index + 1, neighborPosition, newPuzzle)

	backtrack()
