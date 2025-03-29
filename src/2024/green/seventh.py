import itertools


def findBestCandidate(values):
    permutations = [list(v) for v in itertools.permutations('ABCD', 4)]

    tally = {}
    while len(permutations[0]) > 1:
        tally = {}

        for i in range(len(permutations)):
            favorite = permutations[i][0]
            newVotes = values[i]
            tally.update({favorite: tally.get(favorite, 0) + newVotes})

        worst = ''
        for candidate, score in tally.items():
            if worst == '':
                worst = candidate
                continue

            if tally.get(worst) > score:
                worst = candidate

        for comb in permutations:
            comb.remove(worst)

    return (permutations[0][0], tally.get(permutations[0][0]))


if __name__ == '__main__':
    values = [int(v) for v in input().split()]
    result = findBestCandidate(values)
    print(result[0])
    print(result[1])
