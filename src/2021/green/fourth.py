def arabicToRoman(_number_: str) -> str:
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    i = len(num) - 1
    number = int(_number_)
    roman = ''

    while number:
        times = number // num[i]
        number %= num[i]
        roman = roman + (sym[i] * times)
        i -= 1

    if len(roman) == len(_number_):
        return f'{roman} NOT ROMAN-EQUIVALENT'
    else:
        return f'{roman} ROMAN-EQUIVALENT'


if __name__ == '__main__':
    number = input()
    print(arabicToRoman(number))
