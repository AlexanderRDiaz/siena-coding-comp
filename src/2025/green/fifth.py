n, stops = int(input()), [int(v) for v in input().split()]
most = 0


def traverse(idx=0, students=0, times=0):
    global most  # noqa
    if idx == len(stops):
        most = max(most, times)
        return

    if stops[idx] + students <= 100:
        traverse(idx + 1, students + stops[idx], times + 1)
    traverse(idx + 1, students, times)


traverse()

print(most)
