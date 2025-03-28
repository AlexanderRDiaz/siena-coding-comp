import math


def solution():
    n = int(input())

    maxPower = math.floor(math.log2(n))

    for i in range(0, maxPower + 1):
        print(2**i)


solution()
