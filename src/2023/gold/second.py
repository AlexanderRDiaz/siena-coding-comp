def solution():
    start, end, k = int(input()), int(input()), int(input())
    valid = []

    for num in range(start, end + 1):
        _num_ = num
        steps = 0
        while _num_ != 1:
            if _num_ % 2 == 0:
                _num_ //= 2
            else:
                _num_ = (_num_ * 3) + 1
            steps += 1
        if steps == k:
            valid.append(num)

    if len(valid) == 0:
        print('None')

    for num in valid:
        print(num)


solution()
