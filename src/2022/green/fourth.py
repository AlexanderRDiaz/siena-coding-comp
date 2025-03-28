def handleSyllable(syllable):
    vowels = 'aeiou'
    seq = 'idig'

    if syllable[0] in vowels:
        syllable = seq + syllable
    else:
        i = 0
        while syllable[i] not in vowels:
            i += 1
        syllable = syllable[:i] + seq + syllable[i:]
    return syllable


def solution():
    word = input()

    def nextCapitalLetter(index, _word_=word):
        if index > len(_word_):
            return -1

        while index < len(_word_):
            if _word_[index].isupper():
                return index

            index += 1

        return len(_word_)

    start = 0
    end = nextCapitalLetter(1)
    result = ''

    while end != -1:
        syllable = word[start:end].lower()
        result = result + handleSyllable(syllable)
        start, end = end, nextCapitalLetter(end + 1)

    print(result)
