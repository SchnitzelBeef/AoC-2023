from functools import cmp_to_key
from collections import Counter
import numpy as np

def cardTable(card):
    match(card):
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 11
        case 'T':
            return 10
        case _:
            return int(card)

def xKind(cards, x):
    for card in cards:
        if cards[card] == x:
            return 1
    return 0
    
def fullHouse(cards):
    if (xKind(cards, 3) + xKind(cards, 2)) == 2:
        return 1
    return 0

def twoPair(cards):
    i = 0
    for _, count in cards.items():
        if count == 2:
            i += 1
    if i == 2:
        return 1
    return 0

def highest(hand1, hand2):
    for c1, c2 in zip(hand1[0], hand2[0]):
        if cardTable(c1) > cardTable(c2):
            return 1
        if cardTable(c1) < cardTable(c2):
            return -1
    raise()

def handRankWrapper(a, b, hand1, hand2):
    if a ^ b == 1:
        return a - b
    if a & b == 1:
        return highest(hand1, hand2)
    return 0

def highCard(hand1):
    highest = 0
    for c in hand1[0]:
        highest = max(highest, cardTable(c))
    return highest

def comparer(hand1, hand2):
    cards1 = Counter(hand1[0])
    cards2 = Counter(hand2[0])

    if (ret := handRankWrapper(xKind(cards1, 5), xKind(cards2, 5), hand1, hand2)) != 0:
        return ret
    if (ret := handRankWrapper(xKind(cards1, 4), xKind(cards2, 4), hand1, hand2)) != 0:
        return ret
    if (ret := handRankWrapper(fullHouse(cards1), fullHouse(cards2), hand1, hand2)) != 0:
        return ret
    if (ret := handRankWrapper(xKind(cards1, 3), xKind(cards2, 3), hand1, hand2)) != 0:
        return ret
    if (ret := handRankWrapper(twoPair(cards1), twoPair(cards2), hand1, hand2)) != 0:
        return ret
    if (ret := handRankWrapper(xKind(cards1, 2), xKind(cards2, 2), hand1, hand2)) != 0:
        return ret
    if (ret := (highCard(hand1) - highCard(hand2))) != 0:
        return ret
    if (ret := (highest(hand1, hand2)) != 0):
        return ret
    raise()

lines = []

while (line := input()) != "":
    lines.append(line.split())

lines = sorted(lines, key=cmp_to_key(comparer))

sum = 0
for i, line in enumerate(lines):
    print(line[0], line[1])
    sum += (i+1)*int(line[1])

print(sum)
