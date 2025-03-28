import math


def getSuperpowerNumbers(start, end):
    nums = []

    for number in range(start, end + 1):
        _number_ = str(number)
        digits = len(_number_)
        total = 0
        for digit in _number_:
            _digit_ = int(digit)
            total += _digit_**digits
        if math.isclose(int(number), total):
            nums.append(_number_)

    return nums


if __name__ == '__main__':
    start, end = tuple(int(n) for n in input().split(' '))
    numbers = getSuperpowerNumbers(start, end)
    print(len(numbers))
    for n in numbers:
        print(n)
