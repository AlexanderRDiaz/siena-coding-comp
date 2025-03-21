def solution():  # noqa: PLR0912
    value = int(input())
    unit = input()

    if value == 0:
        return print('CALM')
    elif value <= 3:
        return print('LIGHT-AIR')

    if unit == 'MPH':
        if value >= 73:
            print('HURRICANE')
        elif value >= 64:
            print('VIOLENT-STORM')
        elif value >= 55:
            print('STORM')
        elif value >= 47:
            print('SEVERE-GALE')
        elif value >= 39:
            print('GALE')
        elif value >= 32:
            print('NEAR-GALE')
        elif value >= 25:
            print('STRONG-BREEZE')
        elif value >= 19:
            print('FRESH-BREEZE')
        elif value >= 13:
            print('MODERATE-BREEZE')
        elif value >= 8:
            print('GENTLE-BREEZE')
        elif value >= 4:
            print('LIGHT-BREEZE')
    elif unit == 'KNOTS':
        if value >= 64:
            print('HURRICANE')
        elif value >= 56:
            print('VIOLENT-STORM')
        elif value >= 48:
            print('STORM')
        elif value >= 41:
            print('SEVERE-GALE')
        elif value >= 34:
            print('GALE')
        elif value >= 28:
            print('NEAR-GALE')
        elif value >= 22:
            print('STRONG-BREEZE')
        elif value >= 17:
            print('FRESH-BREEZE')
        elif value >= 11:
            print('MODERATE-BREEZE')
        elif value >= 7:
            print('GENTLE-BREEZE')
        elif value >= 4:
            print('LIGHT-BREEZE')


def solution2():
    value = int(input())
    unit = input()

    # Structure where keys represent classifications and inside each is a list if the ranges differ for units.
    # Inside of the classifications with a list, [0] = MPH and [1] = KNOTS.
    classifications = {
        'CALM': range(1),
        'LIGHT-AIR': range(1, 4),
        'LIGHT-BREEZE': [
            range(4, 8),
            range(4, 7),
        ],
        'GENTLE-BREEZE': [
            range(8, 13),
            range(7, 11),
        ],
        'MODERATE-BREEZE': [
            range(13, 19),
            range(11, 17),
        ],
        'FRESH-BREEZE': [
            range(19, 25),
            range(17, 22),
        ],
        'STRONG-BREEZE': [
            range(25, 32),
            range(22, 28),
        ],
        'NEAR-GALE': [
            range(32, 39),
            range(28, 34),
        ],
        'GALE': [
            range(39, 47),
            range(34, 40),
        ],
        'SEVERE-GALE': [
            range(47, 55),
            range(41, 48),
        ],
        'STORM': [
            range(55, 64),
            range(48, 56),
        ],
        'VIOLENT-STORM': [
            range(64, 73),
            range(56, 64),
        ],
    }

    for _class, _range_ in classifications.items():
        if isinstance(_range_, list):
            if unit == 'MPH' and (value in _range_[0]):
                return print(_class)
            elif unit == 'KNOTS' and (value in _range_[1]):
                return print(_class)
        elif value in _range_:
            return print(_class)
    print('HURRICANE')
