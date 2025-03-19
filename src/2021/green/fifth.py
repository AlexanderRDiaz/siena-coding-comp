import math


def main():
	l = int(input())
	r = int(input())
	nums = []
	for number in range(l, r + 1):
		_number_ = str(number)
		digits = len(_number_)
		total = 0
		for digit in _number_:
			_digit_ = int(digit)
			total += _digit_**digits
		if math.isclose(int(number), total):
			nums.append(_number_)

	print(len(nums))
	for num in nums:
		print(num)


main()
