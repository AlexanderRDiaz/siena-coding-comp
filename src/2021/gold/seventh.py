import math


# Finds the position at the "top of the tree", or the start
def topOfTree(position: tuple[int, int]) -> tuple[int, int]:
    if position[1] == 1:
        return position

    return (position[0] - position[1] + 1, 1)


# Gets the nodes that add together to the current node.
def getNextNodes(position: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    return (
        (position[0] + 1, position[1]),
        (position[0] + 1, position[1] + 1),
    )


# Gets the nodes that are a part of the triangle made by this node,
# its adjacent node, and its parent node.
# Ex.      3
#         / \
#        1   2 (from 2's position it gets node 1 and node 3)
def getPreviousNodes(position: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    return (
        (position[0] - 1, position[1] - 1),
        (position[0], position[1] - 1),
    )


def traverseTree(
    values: dict[tuple[int, int], int],
    position: tuple[int, int],
    endDepth: int,
) -> None:
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
        traverseTree(values, pos, endDepth)


# Traverses the tree made to find the value input.
def getValueInTriangleAt(pos: tuple[int, int]) -> dict[tuple[int, int], int]:
    values = {}
    start = topOfTree(pos)
    traverseTree(values, start, pos[1])
    print(f'1/{values.get(pos)}')
    return values


if __name__ == '__main__':
    x, y = tuple([int(n) for n in input().split(' ')])
    denominators = getValueInTriangleAt((x, y))
    print(f'1/{denominators.get((x, y))}')
