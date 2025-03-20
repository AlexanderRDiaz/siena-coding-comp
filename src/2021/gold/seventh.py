import math


def topOfTree(position):
    if position[1] == 1:
        return position

    return (position[0] - position[1] + 1, 1)


def getNextNodes(position):
    return [
        (position[0] + 1, position[1]),
        (position[0] + 1, position[1] + 1),
    ]


def getPreviousNodes(position):
    return (
        (position[0] - 1, position[1] - 1),
        (position[0], position[1] - 1),
    )


def solution():
    x, y = tuple([int(n) for n in input().split(' ')])

    values = {}

    start = topOfTree((x, y))

    def traverse(position=start, endDepth=x):
        if position[0] > endDepth:
            return

        if position[1] == 1:
            print(position[0])
            values.update({position: position[0]})
        else:
            u, l = getPreviousNodes(position)
            uValue, lValue = values.get(u), values.get(l)
            lcm = math.lcm(uValue, lValue)
            numerator = (lcm // uValue) - (lcm // lValue)
            denominator = lcm // numerator
            values.update({position: denominator})

        nextPositions = getNextNodes(position)
        for pos in nextPositions:
            traverse(pos, endDepth)

    traverse()
    print(f'1/{values.get((x, y))}')


solution()
