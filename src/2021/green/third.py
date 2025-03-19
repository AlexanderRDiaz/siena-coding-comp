def solution():  # noqa: PLR0912
    info = input().split(' ')

    speeds = []
    starts = []

    for i in range(6):
        v = int(info[i])
        if i % 2 == 0:
            speeds.append(v)
        else:
            starts.append(v)

    times = []

    for speed, start in zip(speeds, starts, strict=False):
        time = (100 - start) / speed
        times.append(time)

    order = []

    for runnerNum, runnerTime in enumerate(times):
        pos = 0
        for _num_ in order:
            compTime = times[_num_]
            if runnerTime > compTime:
                pos += 1
            elif runnerTime == compTime:
                if _num_ < runnerNum:
                    pos += 1
        order.insert(pos, runnerNum)

    _order_ = ''
    for n in order:
        if len(_order_) == 0:
            _order_ = _order_ + str(n + 1)
        else:
            _order_ = _order_ + ' ' + str(n + 1)
    print(_order_)


solution()
