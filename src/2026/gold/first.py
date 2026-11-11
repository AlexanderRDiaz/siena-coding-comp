def getCategory(unit, value):  # noqa: PLR0911 PLR0912
    d = 'Tropical Depression'
    s = 'Tropical Storm'

    def c(n):
        return 'Category-' + str(n) + ' Hurricane'

    if unit == 'hPa':
        if value > 980:
            return c(1)
        elif value >= 966:
            return c(2)
        elif value >= 946:
            return c(3)
        elif value >= 920:
            return c(4)
        else:
            return c(5)
    elif unit == 'km/h':
        if value < 62:
            return d
        elif value <= 117:
            return s
        elif value <= 153:
            return c(1)
        elif value <= 177:
            return c(2)
        elif value <= 209:
            return c(3)
        elif value <= 249:
            return c(4)
        else:
            return c(5)
    elif unit == 'm':
        if value < 1.2:
            return s
        elif value < 1.8:
            return c(1)
        elif value < 2.7:
            return c(2)
        elif value < 4.0:
            return c(3)
        elif value <= 5.5:
            return c(4)
        else:
            return c(5)


print(getCategory(input(), int(input())))
