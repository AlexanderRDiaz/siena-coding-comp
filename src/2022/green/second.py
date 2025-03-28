def solution():
    year = int(input())

    days = None
    if year % 4 == 0:
        if year % 100 == 0 and (not year % 400 == 0):
            days = 359
        else:
            days = 360
    else:
        days = 359

    if year == 1752:
        print(days - 11)
    else:
        print(days)
