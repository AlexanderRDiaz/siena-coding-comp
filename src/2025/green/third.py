m, n = int(input()), int(input())

solutions = []
for num in range(m, n + 1):
    str_num = str(num)
    if num < 10:
        str_num = '0' + str_num

    i = 1
    valid = False

    while i < len(str_num):
        num1, num2 = int(str_num[:i]), int(str_num[i:])

        if int((num1 + num2) ** 2) == num:
            valid = True
            break

        i += 1

    if valid:
        solutions.append(num)

for num in solutions:
    print(num)

print(len(solutions))
