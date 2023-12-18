import numpy as np
import sys

A = []

while (line := input()) != "":
    A.append([a for a in line])

A = np.asarray(A)

sum = 0

def shiftStonesCycle(A):
    A = np.rot90(A)
    for i in range(4):
        for row in A:
            i = 0
            last_stone = -1
            while i < len(row):
                match row[i]:
                    case '#':
                        last_stone = i
                    case 'O':   
                        row[i] = '.'
                        row[last_stone+1] = 'O'
                        last_stone += 1
                i += 1
        A = np.rot90(A, 3)
    A = np.rot90(A, 3)
    return A.flatten().data.tobytes(), A

def count_stones(A):
    A = np.rot90(A)
    sum = 0
    for row in A:
        i = 0
        for i, stone in enumerate(row):
            if stone == 'O':
                sum += len(row)-i
    return sum

TOTAL = 1000000000

records = {}
cycles_shifted = 0
skipped = False
while cycles_shifted < TOTAL:
    cycles_shifted += 1
    config, A = shiftStonesCycle(A)
    # print(cycles_shifted, "\n" , config, records)
    # print(A)
    if not skipped and config in records:
        skip = cycles_shifted-records[config]
        # print("Skipped: ", cycles_shifted, skip, cycles_shifted + ((TOTAL-cycles_shifted) // skip) * skip)
        cycles_shifted = cycles_shifted + ((TOTAL-cycles_shifted) // skip) * skip
        skipped = True
    else:
        records[config] = cycles_shifted

print("\nCycles Shifted:", cycles_shifted)
print("Count = ", count_stones(A))
