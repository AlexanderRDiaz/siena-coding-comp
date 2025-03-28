def handleLetters(letter):
    global hor, vert, state  # noqa: PLW0603
    if letter == 'L':
        if hor != 0:
            vert = hor
            hor = 0
        else:
            hor = -vert
            vert = 0
    elif letter == 'R':
        if hor != 0:
            vert = -hor
            hor = 0
        else:
            hor = vert
            vert = 0
    elif letter == 'Q':
        return True
    else:
        state = letter
    return False


def solution():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chars = alphabet.lower() + alphabet.upper()

    _input_ = input().upper()
    inputs = []
    while _input_ != 'Q':
        if _input_.isdigit():
            inputs.append(int(_input_))
        else:
            inputs.append(_input_)
        _input_ = input().upper()
    inputs.append(_input_)

    # hor: -1 = left, 0 = n/a, 1 = right
    # vert: -1 = down, 0 = n/a, 1 = up
    global hor, vert, state  # noqa: PLW0603
    state = 'F'
    hor = 1
    vert = 0

    _map_ = [[' ' for _ in range(38)] for _ in range(38)]
    _map_[0][0] = '#'

    def recur(index=0, letter_idx=0, pos=(0, 0)):
        global hor, vert, state  # noqa
        if not isinstance(inputs[index], int):
            end = handleLetters(inputs[index])
            if not end:
                recur(index + 1, letter_idx, pos)
        else:
            if hor:
                if state == 'F':
                    x = pos[0] + hor
                else:
                    x = pos[0] - hor
                y = pos[1]
            else:
                if state == 'F':
                    y = pos[1] - vert
                else:
                    y = pos[1] + vert
                x = pos[0]

            _map_[y][x] = chars[letter_idx]
            inputs[index] -= 1

            if inputs[index]:
                recur(index, letter_idx + 1, (x, y))
            else:
                recur(index + 1, letter_idx + 1, (x, y))

    recur()

    print('*' * 40)
    for row in _map_:
        print(f'*{"".join(row)}*')
    print('*' * 40)


solution()
