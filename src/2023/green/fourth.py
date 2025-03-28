def solution():
    n = int(input())
    factors = []

    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    _sum_ = 0
    for factor in factors:
        _sum_ += factor

    if _sum_ > n:
        print(f'{n} Abundant')
    elif _sum_ == n:
        print(f'{n} Perfect')
    else:
        print(f'{n} Deficient')
