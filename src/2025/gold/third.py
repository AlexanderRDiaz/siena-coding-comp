units = ['G', 'M', 'K', 'B']
values = [2**30, 2**20, 2**10, 2**0]

n = int(input())
result = ''
for value, unit in zip(values, units, strict=False):
    unitValue = int(n // value)
    n = n % value

    if unitValue == 0:
        continue

    if not result:
        result = f'{unitValue} {unit}'
    else:
        result = result + f' {unitValue} {unit}'

print(result)
