import math


def solution():
    binary = input()

    num = 0
    i = 0
    while i < len(binary):
        power = len(binary) - i - 1
        if binary[i] == '1':
            num += 2 ** (power)
        i += 1
    denom = 2 ** len(binary) - 1

    gcd = math.gcd(num, denom)
    num, denom = num // gcd, denom // gcd

    print(f'{num}/{denom}')
