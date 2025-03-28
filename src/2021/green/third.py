def getOrder(info: list[int]) -> str:  # noqa: PLR0912
    times = []

    for speed, start in zip(*[iter(info)] * 2, strict=False):
        time = (100 - start) / speed
        times.append(time)

    order = []

    for runnerNum, runnerTime in enumerate(times):
        pos = 0
        for competitorNum in order:
            competitorTime = times[competitorNum]
            if (runnerTime > competitorTime) or (
                runnerTime == competitorTime and competitorNum < runnerNum
            ):
                pos += 1
        order.insert(pos, runnerNum)

    return ''.join([str(runner + 1) + ' ' for runner in order])


if __name__ == '__main__':
    info = [int(n) for n in input().split()]
    print(getOrder(info))
