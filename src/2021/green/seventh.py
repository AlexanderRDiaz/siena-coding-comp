from copy import deepcopy


# Resolve hints into easy to work with data structures.
def formatTopBottomHints(
    top: list[str],
    bottom: list[str],
) -> tuple[list[list[str]], dict[str, tuple[tuple[int, int], ...]]]:
    columns = []
    temp1 = top.copy()
    temp1.pop(len(top) - 1)
    temp1.pop(0)

    temp2 = bottom.copy()
    temp2.pop(len(bottom) - 1)
    temp2.pop(0)

    for i in range(5):
        columns.append([temp1[i], temp2[i]])

    diagonal1 = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )

    diagonal2 = (
        (0, 4),
        (1, 3),
        (2, 2),
        (3, 1),
        (4, 0),
    )

    diagonals = {
        top[0]: diagonal1,
        top[6]: diagonal2,
        bottom[0]: diagonal2,
        bottom[6]: diagonal1,
    }

    return columns, diagonals


# Get neighboring positions by doing simple math, and removing invalid places.
def getNeighbors(position: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    neighbors = [
        (position[0] - 1, position[1] - 1),
        (position[0] - 1, position[1]),
        (position[0] - 1, position[1] + 1),
        (position[0], position[1] - 1),
        (position[0], position[1] + 1),
        (position[0] + 1, position[1] - 1),
        (position[0] + 1, position[1]),
        (position[0] + 1, position[1] + 1),
    ]

    i = 0
    while i < len(neighbors):
        row, column = neighbors[i][0], neighbors[i][1]

        if not (0 <= row < 5) or not (0 <= column < 5):
            neighbors.pop(i)
        else:
            i += 1

    return tuple(neighbors)


# Get all possible letters that fit the position according to the hints given.
def resolveHints(
    position: tuple[int, int],
    rows: list[list[str]],
    columns: list[list[str]],
    diagonals: dict[str, tuple[tuple[int, ...], ...]],
) -> tuple[list[str], list[str], list[str]]:
    allHints = []
    allHints.extend(rows[position[0]])
    allHints.extend(columns[position[1]])

    diagonalHints = []
    for char, diagPoses in diagonals.items():
        for dPos in diagPoses:
            sameRow = dPos[0] == position[0]
            sameColumn = dPos[1] == position[1]
            if sameRow and sameColumn:
                diagonalHints.append(char)

    return (rows[position[0]], columns[position[1]], diagonalHints)


def traversePuzzle(  # noqa
    solutions: list[list[list[str]]],
    puzzle: list[list[str]],
    position: tuple[int, int],
    index: int,
    rowHint: list[list[str]],
    columnHint: list[list[str]],
    diagonalHint: dict[str, tuple[tuple[int, int], ...]],
) -> None:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXY'

    if index == len(letters):
        return solutions.append(puzzle)
    elif index == 0:
        puzzle[position[0]][position[1]] = 'A'
        index += 1

    for neighbor in getNeighbors(position):
        row, column = neighbor[0], neighbor[1]
        hints = resolveHints(neighbor, rowHint, columnHint, diagonalHint)
        valid = letters[index] in hints
        if not puzzle[row][column] and valid:
            newPuzzle = deepcopy(puzzle)
            newPuzzle[row][column] = letters[index]
            traversePuzzle(
                solutions,
                newPuzzle,
                neighbor,
                index + 1,
                rowHint,
                columnHint,
                diagonalHint,
            )


def solvePuzzle(
    top: list[str],
    rows: list[list[str]],
    bottom: list[str],
    start: tuple[int, int],
) -> list[list[list[str]]]:
    columns, diagonals = formatTopBottomHints(top, bottom)
    emptyPuzzle = [['' for _ in range(5)] for _ in range(5)]
    solutions = []

    traversePuzzle(solutions, emptyPuzzle, start, 0, rows, columns, diagonals)

    return solutions


if __name__ == '__main__':
    top = list(input().upper())
    rows = [list(input().upper()) for _ in range(5)]
    bottom = list(input().upper())
    _start_ = input().split()
    start = (int(_start_[0]), int(_start_[1]))
    solutions = solvePuzzle(top, rows, bottom, start)
    if len(solutions) > 1:
        print('MULTIPLE SOLUTIONS: THIS IS NOT A VALID INPUT!')
    for row in solutions[0]:
        print(''.join(row))
