def permute(string):
    permutations = []

    if len(string) == 1:
        return string

    for index, letter in enumerate(string):
        for permutation in permute(string[:index] + string[index + 1 :]):
            permutations.append(letter + permutation)

    return permutations


if __name__ == '__main__':
    string = input()
    print(permute(string))
