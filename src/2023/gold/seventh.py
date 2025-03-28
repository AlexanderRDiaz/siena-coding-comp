def getNeighbors(position: tuple[int, int]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    movements = [
        (-1, -1),
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 0),
        (1, 1),
    ]

    neighbors = []

    for move in movements:
        neighbor = (position[0] + move[0], position[1] + move[1])
        jumpPosition = (neighbor[0] + move[0], neighbor[1] + move[1])
        neighbors.append((neighbor, jumpPosition))

    return neighbors


def generatePuzzle(rows: int) -> list[list[int]]:
    puzzle = [[] for _ in range(rows)]
    row = 0
    i = 1

    while row < rows:
        puzzle[row].append(i)
        i += 1
        if len(puzzle[row]) == row + 1:
            row += 1

    return puzzle


def sortJumps(old: list[str]) -> list[str]:
    new = []

    for jump in old:
        if len(new) == 0:
            new.append(jump)
            continue

        i = -1
        sJump, *_ = tuple([int(v) for v in jump.split('-')])
        s_jump = 0
        while sJump > s_jump:
            i += 1
            s_jump, *_ = tuple([int(v) for v in old[i].split('-')])
        new.insert(i, jump)

    return new


def findBestSolution(solutions: list[tuple[list[str], list[int]]]) -> tuple[list[str], list[int]]:
    bestIdx = 0
    for idx, sol in enumerate(solutions):
        bestJumps = solutions[bestIdx][0]
        bestPegs = solutions[bestIdx][1]
        jumps = sol[0]
        pegs = sol[1]

        if (len(jumps) > len(bestJumps)) or (
            len(jumps) == len(bestJumps) and len(pegs) < len(bestPegs)
        ):
            continue
        elif len(jumps) < len(bestJumps) or len(pegs) > len(bestPegs):
            bestIdx = idx
            continue
        else:
            for best, jump in zip(bestJumps, jumps, strict=False):
                if jump == best:
                    continue

                sJump, eJump = tuple([int(v) for v in jump.split('-')])
                sBest, eBest = tuple([int(v) for v in best.split('-')])

                if sBest < sJump:
                    break

                if sJump < sBest:
                    bestIdx = idx
                elif sJump == sBest:
                    if eJump < eBest:
                        bestIdx = idx

    return solutions[bestIdx]


def solvePegs(pegs: list[int]) -> list[str]:
    puzzle = generatePuzzle(6)
    solutions = []

    def getPositionForNode(value: int) -> tuple[int, int]:
        nonlocal puzzle
        for rowPos, row in enumerate(puzzle):
            for columnPos, _value_ in enumerate(row):
                if _value_ == value:
                    return (rowPos, columnPos)
        return (0, 0)

    def traversePuzzle(jumps, pegs=pegs):
        nonlocal puzzle, solutions

        jumpFound = False
        for peg in pegs:
            position = getPositionForNode(peg)
            if position == (0, 0):
                continue
            for neighbor, jumpPosition in getNeighbors(position):
                if (
                    (len(puzzle) <= neighbor[0])
                    or (len(puzzle[neighbor[0]]) <= neighbor[1])
                    or (
                        (len(puzzle) <= jumpPosition[0])
                        or (len(puzzle[jumpPosition[0]]) <= jumpPosition[1])
                    )
                ):
                    continue

                neighborNode = puzzle[neighbor[0]][neighbor[1]]

                if neighborNode not in pegs:
                    continue

                jumpFound = True
                newPegs = pegs.copy()
                newPegs.remove(neighborNode)
                newPegs.remove(peg)

                jumpNode = puzzle[jumpPosition[0]][jumpPosition[1]]
                newPegs.append(jumpNode)

                newJumps = jumps.copy()
                newJumps.append(f'{peg}-{jumpNode}')

                newPegs.sort()

                traversePuzzle(newJumps, newPegs)

        if not jumpFound:
            solutions.append((sortJumps(jumps), pegs))

    traversePuzzle([])
    return findBestSolution(solutions)[0]


if __name__ == '__main__':
    (n, *pegs) = tuple([int(v) for v in input().split()])
    pegs = list(pegs)
    pegs.sort()
    solution = solvePegs(pegs)
    print(len(solution))
    for v in solution:
        print(v)
