def getCondition(value: int, unit: str) -> str:  # noqa: PLR0912
    condition = ''

    if value == 0:
        condition = 'CALM'
    elif value <= 3:
        condition = 'LIGHT-AIR'
    elif unit == 'MPH':
        if value >= 73:
            condition = 'HURRICANE'
        elif value >= 64:
            condition = 'VIOLENT-STORM'
        elif value >= 55:
            condition = 'STORM'
        elif value >= 47:
            condition = 'SEVERE-GALE'
        elif value >= 39:
            condition = 'GALE'
        elif value >= 32:
            condition = 'NEAR-GALE'
        elif value >= 25:
            condition = 'STRONG-BREEZE'
        elif value >= 19:
            condition = 'FRESH-BREEZE'
        elif value >= 13:
            condition = 'MODERATE-BREEZE'
        elif value >= 8:
            condition = 'GENTLE-BREEZE'
        elif value >= 4:
            condition = 'LIGHT-BREEZE'
    elif unit == 'KNOTS':
        if value >= 64:
            condition = 'HURRICANE'
        elif value >= 56:
            condition = 'VIOLENT-STORM'
        elif value >= 48:
            condition = 'STORM'
        elif value >= 41:
            condition = 'SEVERE-GALE'
        elif value >= 34:
            condition = 'GALE'
        elif value >= 28:
            condition = 'NEAR-GALE'
        elif value >= 22:
            condition = 'STRONG-BREEZE'
        elif value >= 17:
            condition = 'FRESH-BREEZE'
        elif value >= 11:
            condition = 'MODERATE-BREEZE'
        elif value >= 7:
            condition = 'GENTLE-BREEZE'
        elif value >= 4:
            condition = 'LIGHT-BREEZE'

    return condition


if __name__ == '__main__':
    value, unit = int(input()), input()
    print(getCondition(value, unit))
