from collections import Counter


def prime_factors(n):
    factors = []

    i = 2

    while (i**2) <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    return factors


def solution():
    minimum = int(input())
    maximum = int(input()) + 1

    valid = []

    for n in range(minimum, maximum):
        factors = prime_factors(n)

        if factors[0] == n:
            continue

        c_factors = Counter(factors)

        most = c_factors.most_common(1)

        if most[0][1] > 1:
            continue

        hippie = all((n - 1) % (factor - 1) == 0 for factor in factors)

        if hippie:
            valid.append(n)

    if not valid:
        print('None')

    for num in valid:
        print(num)


solution()
