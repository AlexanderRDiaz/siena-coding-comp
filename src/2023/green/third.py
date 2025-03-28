def solution():
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]

    monthIndex = int(input()) - 1
    day = input()

    if day in ('1', '21', '31'):
        day = day + 'st'
    elif day in ('2', '22'):
        day = day + 'nd'
    elif day in ('3', '23'):
        day = day + 'rd'
    else:
        day = day + 'th'

    print(f'{months[monthIndex]} {day} 2023')


solution()
