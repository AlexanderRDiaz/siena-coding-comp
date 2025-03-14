import math as math
def main():
    l = int(input())
    r = int(input())
    nums = list()
    for number in range(l, r+1):
        number = str(number)
        digits = len(number)
        total = 0
        for digit in number:
            digit = int(digit)
            total += digit**digits
        if math.isclose(int(number), total):
            nums.append(number)

    print(len(nums))
    for num in nums:
        print(num)

main()
