def main():
	number = int(input())
	num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
	sym = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
	i = len(num)
	roman = ''
	while number:
		times = number // num[i]
		number %= num[i]
		roman = roman + (sym[i] * times)
		i -= 1
	print(roman)


main()
