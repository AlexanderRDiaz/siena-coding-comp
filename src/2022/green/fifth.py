def resolveHints(guess, answer):
    hint = ''
    _map_ = {}
    i = 0

    def incrementHash(key):
        stored = _map_.get(key)
        if stored:
            _map_.update({key: stored + 1})
        else:
            _map_.update({key: 1})

    while i < len(answer):
        if guess[i] in answer:
            hint = hint + 'G' if (guess[i] == answer[i]) else hint + 'Y'
            incrementHash(answer)
        else:
            hint = hint + 'D'

        i += 1

    return hint


def solution():
    answer = input()
    times = int(input())
    hints = []

    for _ in range(times):
        guess = input()
        hints.append(resolveHints(guess, answer))

    for hint in hints:
        print(hint)
