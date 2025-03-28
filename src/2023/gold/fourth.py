def solution():
    length = int(input())
    students = list(range(1, length + 1))
    step = int(input())

    i = -1
    while len(students) > 2:
        i += step

        if i > len(students) - 1:
            i %= len(students)

        students.pop(i)
        i -= 1

    print(f'{students[0]} {students[1]}')


solution()
