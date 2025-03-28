import math


def solution():
    maximum = int(input())

    largestH, bestA2 = 0, 0
    for a2 in range(2, 100):
        h = 1

        while True:
            h += 1
            r = h

            r %= a2
            used = math.floor(h / a2)
            if r > (maximum - used):
                break

        if h > largestH:
            largestH = h - 1
            bestA2 = a2
    print(largestH)
    print(f'1 {bestA2}')
