""""""

"""BDRUOHNZVEXIJYWTCKGFQSMAPL"""
"""ca2t"""
"""d27o-2g"""


"""QWERTYUIOPASDFGHJKLZXCVBNM"""
"""transfinder"""
"""edkyln52hymcd"""
decoded = [chr(v) for v in range(ord('a'), ord('z') + 1)]
encoded = list(input())
seq = input()


def shift(n):
    new = ['' for _ in range(len(encoded))]
    i = 0
    while i < len(encoded):
        idx = (i + n) % len(encoded)
        new[idx] = encoded[i]
        i += 1
    return new


i = 0
result = ''
while i < len(seq):
    if seq[i].isdigit() or seq[i] in '+-':
        idx = i
        while seq[idx].isdigit() or seq[idx] in '+-':
            idx += 1
        encoded = shift(int(eval(seq[i:idx])))
        i = idx
    elif seq[i].isalpha():
        idx = decoded.index(seq[i])
        result = result + encoded[idx]
        i += 1

print(result)
