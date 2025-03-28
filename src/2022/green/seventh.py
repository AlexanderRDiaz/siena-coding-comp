def solution():
    p = int(input())
    n = int(input())

    routes = []
    for _ in range(n):
        k = int(input())
        route = [int(n) for n in input().split()]
        if len(route) != k:
            raise RuntimeError('Not K Routes for stations')
        routes.append(route)

    global counter  # noqa: PLW0603
    counter = 0

    def traverse(station):
        if station == p:
            global counter  # noqa: PLW0603
            counter += 1
            return

        for _route_ in routes:
            if not _route_.count(station):
                continue
            i = _route_.index(station)
            traverse(_route_[i + 1])

    for route in routes:
        if route[0] != 1:
            continue
        traverse(route[1])

    print(counter)


solution()
