import math as math

def square():
    n = int(input())
    result = (n * (n + 1) * ((2 * n) + 1))
    print(result)

def fifthPower():
    x = int(input())
    y = int(input())
    result = math.pow((x + y), 5)
    print(result)

def cincoDeMayo():
    n = int(input())
    result = math.floor(((3 * n) - 1) / 2)
    print(result)

def gradeConverter():
    n = int(input())
    g = None
    if n >= 95:
        g = "A+"
    elif n >= 90:
        g = "A"
    elif n >= 85:
        g = "A-"
    elif n >= 80:
        g = "B+"
    elif n >= 75:
        g = "B"
    elif n >= 70:
        g = "B-"
    elif n >= 65:
        g = "C+"
    elif n >= 60:
        g = "C"
    elif n >= 55:
        g = "C-"
    elif n >= 50:
        g = "D+"
    elif n >= 45:
        g = "D"
    elif n >= 40:
        g = "D-"
    else:
        g = "F"
    
    print(g)

def timeIs():
    printQueue = list()
    n = int(input())
    ys = 365 * 24 * 60 * 60
    ds = ys // 365
    hs = ds // 24
    ms = hs // 60
    
    y = math.floor(n/ys)
    n = n - (ys * y)
    if len(printQueue) == 0 or y != 0:
        printQueue.append(f"{y} years")
    
    d = math.floor(n/ds)
    n = n - (ds * d)
    if len(printQueue) != 0 or d != 0:
        printQueue.append(f"{d} days")
    
    h = math.floor(n/hs)
    n = n - (hs * h)
    if len(printQueue) != 0 or h != 0:
        printQueue.append(f"{h} hours")
    
    m = math.floor(n/ms)
    n = n - (ms * m)
    if len(printQueue) != 0 or m != 0:
        printQueue.append(f"{m} minutes")
    printQueue.append(f"{n} seconds")
        
    for string in printQueue:
        print(string)

def bestOfTwo():
    numberNames = [
        "ACE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE",
        "TEN",
    ]
    signNames = {
        "C": "CLUBS",
        "D": "DIAMONDS",
        "H": "HEARTS",
        "S": "SPADES"
    }
    cards = input()
    info = cards.split(" ")
    num1 = int(info[0])
    sign1 = info[1]
    num2 = int(info[2])
    sign2 = info[3]

    compare = ["C", "D", "H", "S"]
    value1 = 0
    value2 = 0

    for number, power in enumerate(compare):
        if sign1 == power:
            value1 = number
        if sign2 == power:
            value2 = number
            
    compare1 = 11 if num1 == 1 else num1
    compare2 = 11 if num2 == 1 else num2
    
    if compare1 > compare2:
        print(f"{numberNames[num1-1]} OF {signNames.get(sign1)}")
    elif compare2 > compare1:
        print(f"{numberNames[num2-1]} OF {signNames.get(sign2)}")
    else:
        if value1 > value2:
            print(f"{numberNames[num1-1]} OF {signNames.get(sign1)}")
        elif value2 > value1:
            print(f"{numberNames[num2-1]} OF {signNames.get(sign2)}")

def poker():
    ranks = input()
    matches = list()

    for i in range(2, 15):
        number = str(i)
        length = len(number)
        counter = 0 

        for k in range(len(ranks)):
            if length == 1:
                counter = counter + 1 if ranks[k] == number else counter
            else:
                counter = counter + 1 if ranks[k:k+(length-1)] else counter
        if counter == 2:
            matches.append("Pair")
        elif counter == 3:
            matches.append("Three-of-a-Kind")
        elif counter == 4:
            matches.append("Four-of-a-Kind")

    if len(matches) == 0:
        return print("No-Matches")

    pairs = 0
    for match in matches:
        if match == "Pair":
            pairs += 1

    if pairs == 1:
        return print("One-Pair")
    elif pairs == 2:
        return print("Two-Pairs")

    if len(matches) == 1:
        print(matches[0])

def textProcess(string):
    y = 0
    w = 0 
    c = 0
    v = 0

    for letter in string:
        if letter.lower() in "bcdfghjklmnpqrxtvx":
            c += 1
        elif letter.lower() == "w":
            w += 1
        elif letter.lower() == "y":
            y += 1
        else:
            v += 1

    print(f"{c} consonants")
    print(f"{v} vowels")
    print(f"{y} Ys")
    print(f"{w} Ws")
