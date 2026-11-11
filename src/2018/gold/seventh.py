import sys
from copy import deepcopy

sys.setrecursionlimit(10000)

"""
GIVEN:

Input:			Output:
7 7 5
6 0 1 2			NENNNNE
4 0 5 2			NNNNEEESSWSSS
0 5 5 5			WSSSWSSSEE
6 1 0 6			EEEEENNNNNN
1 5 4 4			SSSW
"""

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
cardinals = ['N', 'W', 'S', 'E']

rows, columns, k = [int(v) for v in input().split(' ')]
grid = [[0 for _ in range(columns)] for _ in range(rows)]
solutions = []
paths = [''] * k
starts = []
ends = []
print(grid)
for _ in range(k):
    values = input().split(' ')
    start, end = [(int(x), int(c)) for x, c in zip(values[::2], values[1::2], strict=False)]
    starts.append(start)
    ends.append(end)
starts.append((-1, -1))


def move(position, magnitude):
    return (position[0] + magnitude[0], position[1] + magnitude[1])


def connected(p1, p2):
    distance = (abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))
    return (distance[0] == 0 or distance[1] == 0) and (distance[0] == 1 or distance[1] == 1)


def out_of_bounds(p):
    return not (0 <= p[0] < rows) or not (0 <= p[1] < columns)


def intersects(p):
    return grid[p[0]][p[1]] != 0


def solve(position=starts[0], routeN=0):
    if routeN > k - 1:
        return solutions.append(deepcopy(paths))

    for direction, cardinal in zip(moves, cardinals, strict=False):
        newPos = move(position, direction)
        if out_of_bounds(newPos):
            continue
        if intersects(newPos):
            continue

        x, c = newPos
        grid[x][c] = routeN
        paths[routeN] = paths[routeN] + cardinal

        if connected(ends[routeN], newPos):
            solve(starts[routeN + 1], routeN + 1)
        else:
            solve(newPos, routeN)

        grid[x][c] = 0
        paths[routeN] = paths[routeN][:-1]


solve()

if len(solutions) == 0:
    print('NO SOLUTION')
for s in solutions:
    for path in s:
        print(path)
