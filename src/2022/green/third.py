def solution():
    ranks = [
        'MARSHAL',
        'GENERAL',
        'COLONEL',
        'MAJOR',
        'CAPTAIN',
        'LIEUTENANT',
        'SERGEANT',
        'MINER',
        'SCOUT',
        'SPY',
    ]

    r = ' REMOVED'

    a, d = input(), input()

    if d == 'FLAG':
        return print(d + r)

    if a == ranks[7] and d == 'BOMB':
        return print(d + r)
    elif d == 'BOMB':
        return print(a + r)

    if a == ranks[9] and d == ranks[0]:
        return print(d + r)

    if a == d:
        return print('BOTH' + r)

    aRank = ranks.index(a)
    dRank = ranks.index(d)

    if aRank > dRank:
        print(a + r)
    else:
        print(d + r)
