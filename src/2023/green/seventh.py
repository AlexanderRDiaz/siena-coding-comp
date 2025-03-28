def solution():
    factors = []

    n = int(input())

    for factor1 in range(1, n + 1):
        for factor2 in range(1, n + 1):
            factor3 = n // (factor1 * factor2)

            if (factor1 * factor2 * factor3) == n:
                _factors_ = [factor1, factor2, factor3]
                _factors_.sort()
                different = True
                for factorSet in factors:
                    sameFirst = _factors_[0] == factorSet[0]
                    sameSecond = _factors_[1] == factorSet[1]
                    sameThird = _factors_[2] == factorSet[2]
                    if sameFirst and sameSecond and sameThird:
                        different = False

                if different:
                    factors.append(_factors_)

    print(f'{n} has {len(factors)} factor triples')
    for factor in factors:
        string = f'{factor[0]} {factor[1]} {factor[2]}'
        print(string)


solution()
