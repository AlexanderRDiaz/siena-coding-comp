def getCondition(value: int, unit: str) -> str:  # noqa: PLR0912
    condition = ''

    if value == 0:
        condition = 'CALM'
    elif value <= 3:
        condition = 'LIGHT-AIR'
    elif unit == 'MPH' and value <= 72:
        if value <= 7:
            condition = 'LIGHT-BREEZE'
        elif value <= 12:
            condition = 'GENTLE-BREEZE'
        elif value <= 18:
            condition = 'MODERATE-BREEZE'
        elif value <= 24:
            condition = 'FRESH-BREEZE'
        elif value <= 31:
            condition = 'STRONG-BREEZE'
        elif value <= 38:
            condition = 'NEAR-GALE'
        elif value <= 46:
            condition = 'GALE'
        elif value <= 54:
            condition = 'SEVERE-GALE'
        elif value <= 63:
            condition = 'STORM'
        elif value <= 72:
            condition = 'VIOLENT-STORM'
    elif unit == 'KNOTS' and value <= 63:
        if value <= 6:
            condition = 'LIGHT-BREEZE'
        elif value <= 10:
            condition = 'GENTLE-BREEZE'
        elif value <= 16:
            condition = 'MODERATE-BREEZE'
        elif value <= 21:
            condition = 'FRESH-BREEZE'
        elif value <= 27:
            condition = 'STRONG-BREEZE'
        elif value <= 33:
            condition = 'NEAR-GALE'
        elif value <= 40:
            condition = 'GALE'
        elif value <= 47:
            condition = 'SEVERE-GALE'
        elif value <= 55:
            condition = 'STORM'
        elif value <= 63:
            condition = 'VIOLENT-STORM'
    else:
        condition = 'HURRICANE'

    return condition


if __name__ == '__main__':
    value, unit = int(input()), input()
    print(getCondition(value, unit))
