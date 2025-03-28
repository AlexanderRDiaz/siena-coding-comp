def solution():
    _items_ = ['HAT', 'SHIRT', 'PANTS', 'SOCKS']
    _colors_ = ['RED', 'BLUE', 'GREEN', 'YELLOW']
    restrictions = []
    validCombs = []

    n = int(input())
    for _ in range(n):
        c1, i1, c2, i2 = input().upper().split()
        restrictions.append([f'{c1}_{i1}', f'{c2}_{i2}'])

    def validComb(combination):
        items = combination.split()

        for restriction in restrictions:
            temp = restriction.copy()

            for item in items:
                i = 0
                while i < len(temp):
                    if temp[i] == item:
                        temp.pop(i)
                    else:
                        i += 1

            if len(temp) == 0:
                return False
        return True

    def getCombs(comb='', index=0):
        if index == len(_items_):
            if validComb(comb):
                validCombs.append(comb)
            return

        for color in _colors_:
            if len(comb) == 0:
                getCombs(comb + f'{color}_{_items_[index]}', index + 1)
            else:
                getCombs(comb + f' {color}_{_items_[index]}', index + 1)

    getCombs()
    print(len(validCombs))
