def main():
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

	for i, time in enumerate(times):
		c = False
		for pos, runner in enumerate(order):
			if times[runner] > time:
				newPos = 0 if pos - 1 < 0 else pos - 1
				order.insert(newPos, i)
				c = True
				break
		if not c:
			order.append(i)

	order = [n + 1 for n in order]
	print(f'{order[0]} {order[1]} {order[2]}')


main()
