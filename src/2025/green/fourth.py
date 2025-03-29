p = int(input())

count = 0
for a in range(1, (p // 2) + 1):
    for b in range(a, (p - a) // 2 + 1):
        c = p - a - b
        if a + b > c:
            count += 1

print(count)
