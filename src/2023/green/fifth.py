def solution():
    for num1 in range(100, 1000):
        for num2 in range(100, 1000):
            if num1 * num2 > 99999:
                continue
            string = str(num1) + str(num2)
            for digit in str(num2):
                string = string + str(num1 * int(digit))
            string = string + str(num1 * num2)

            exception = ''
            for digit in '1234567890':
                count = string.count(digit)
                if count > 2:
                    if len(exception) == 0:
                        exception = f' except {digit} which appears {count} times'
                    else:
                        exception = exception + f' {digit} which appears {count} times'

            print(f'{num1} x {num2}: each digit appears exactly 2 times{exception}')


solution()
