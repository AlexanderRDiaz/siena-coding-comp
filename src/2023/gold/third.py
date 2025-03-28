from collections import Counter


def solution():
    values = []
    for _ in range(5):
        values.append(int(input()))
    values.sort()

    counted = Counter(values)
    selected = counted.most_common(2)

    if selected[0][1] == 5:
        print(1000 + sum(values))
    elif selected[0][1] == 4:
        print(600 + (selected[0][0] * 4))
    elif selected[0][1] == 3:
        if selected[1][1] == 2:
            print(400 + sum(values))
        else:
            print(300 + (selected[0][0] * 3))
    elif selected[0][1] == 2:
        if selected[1][1] == 2:
            print(200 + (selected[0][0] * 2) + (selected[1][0] * 2))
        else:
            print(100 + (selected[0][0] * 2))
    elif all(values[i] == (values[i + 1] - 1) for i in range(len(values) - 1)):
        print(500 + sum(values))
    else:
        print(sum(values))


solution()
