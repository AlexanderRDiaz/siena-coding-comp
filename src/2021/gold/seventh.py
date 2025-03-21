import math


# This is a complex problem, which uses tree traversal and recursion.
# Examples are found in extras


# Finds the position at the "top of the tree", or the start
def topOfTree(position):
    if position[1] == 1:
        return position

    return (position[0] - position[1] + 1, 1)


# Gets the nodes that add together to the current node.
def getNextNodes(position):
    return [
        (position[0] + 1, position[1]),
        (position[0] + 1, position[1] + 1),
    ]


# Gets the nodes that are a part of the triangle made by this node,
# its adjacent node, and its parent node.
# Ex.      3
#         / \
#        1   2 (from 2's position it gets node 1 and node 3)
def getPreviousNodes(position):
    return (
        (position[0] - 1, position[1] - 1),
        (position[0], position[1] - 1),
    )


# Traverses the tree made to find the value input.
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
            lcm = math.lcm(uValue, lValue)  # pyright: ignore
            numerator = (lcm // uValue) - (lcm // lValue)  # pyright: ignore
            denominator = lcm // numerator
            values.update({position: denominator})

        nextPositions = getNextNodes(position)
        for pos in nextPositions:
            traverse(pos, endDepth)

    traverse()
    print(f'1/{values.get((x, y))}')
