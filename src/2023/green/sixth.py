def solution():
    alphabet = 'abcefghijklmnopqrstuvwxyz'

    sequence = input().lower()

    for letter in sequence:
        if letter in alphabet:
            index = alphabet.index(letter)
            alphabet = alphabet[:index] + alphabet[index + 1 :]

    if not alphabet:
        print('PANGRAM')
    else:
        print(alphabet.upper())


solution()
