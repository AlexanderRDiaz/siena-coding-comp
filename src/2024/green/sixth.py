def calculateIntersection(stops: list[int]) -> list[int]:
    bus1 = [0, 0]
    bus2 = [len(stops) - 1, 0]
    time = 1
    while bus1[0] != bus2[0]:
        if stops[bus1[0]]:
            stops[bus1[0]] -= 1
            bus1[1] += 1
        else:
            bus1[0] += 1
        if stops[bus2[0]]:
            stops[bus2[0]] -= 1
            bus2[1] += 1
        else:
            bus2[0] -= 1
        time += 1

    return [bus1[0] + 1, time, bus1[1], bus2[1]]


if __name__ == '__main__':
    n = int(input())
    stops = [int(input()) for _ in range(n)]
    result = calculateIntersection(stops)
    print(f'{result[0]} {result[1]} {result[2]} {result[3]}')
