import sys
from copy import deepcopy

"""
7 7 5
5 2 2 4
6 0 1 4
1 1 2 3
0 3 6 4
1 5 3 3
"""

temp_points = [
    [5, 2, 2, 4],
    [6, 0, 1, 4],
    [1, 1, 2, 3],
    [0, 3, 6, 4],
    [1, 5, 3, 3],
]

# rows, columns, k = [int(v) for v in input().split(' ')]
rows, columns, k = 7, 7, 5
grid: list[list[int | str]] = [[0 for _ in range(columns)] for _ in range(rows)]
starts = [(0, 0)]
ends = [(0, 0)]
for i in range(1, k + 1):
    # s1, e1, s2, e2 = [int(v) for v in input().split(' ')]
    s1, e1, s2, e2 = temp_points[i - 1]
    grid[s1][e1] = i
    grid[s2][e2] = i
    starts.append((s1, e1))
    ends.append((s2, e2))

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
solutions = []


def addPos(pos: tuple[int, int], change: tuple[int, int]):
    return (pos[0] + change[0], pos[1] + change[1])


def connectionCheck(pos: tuple[int, int], cur: int):
    checkPos = ends[cur]

    distance = (abs(checkPos[0] - pos[0]), abs(checkPos[1] - pos[1]))

    return (distance[0] == 0 or distance[1] == 0) and (distance[0] == 1 or distance[1] == 1)


def formatGrid(_grid: list[list[int | str]]):
    return '\n'.join([' '.join([str(v) for v in row]) for row in _grid])


def recurse(pos: tuple[int, int], cur: int):
    for i in range(len(dirs)):
        x, y = addPos(pos, dirs[i])
        if x < 0 or x >= rows or y < 0 or y >= columns:
            continue
        if grid[x][y] != 0:
            continue

        grid[x][y] = chr(cur + ord('a') - 1)
        if connectionCheck((x, y), cur):
            if cur + 1 > k:
                solutions.append(deepcopy(grid))
                continue
            recurse(starts[cur + 1], cur + 1)
        else:
            recurse((x, y), cur)
        grid[x][y] = 0


recurse(starts[1], 1)

if len(solutions) == 0:
    print('no solutions')
for sol in solutions:
    print(formatGrid(sol))
