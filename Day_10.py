import numpy as np
import sys
import time

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

# (y, x)
pieces = {
    '|' : [DOWN , UP   ],
    '-' : [RIGHT, LEFT ],
    'L' : [UP   , RIGHT],
    'J' : [UP   , LEFT ], 
    '7' : [LEFT , DOWN ],
    'F' : [RIGHT, DOWN ],
}

directions = {
    0 : RIGHT,
    1 : DOWN,
    2 : LEFT,
    3 : UP
}

def negTuple(X):
    return X[0] * -1, X[1] * -1

def addTuples(X, Y):
    return X[0] + Y[0], X[1] + Y[1]

Pipes = [] 
i = 0

while (line := input()) != "":
    Pipes.append(['.']*(len(line)*2+1))
    Pipes.append([])
    for j, x in enumerate(line):
        if x == 'S':
            start_pos = (i*2+1, j*2+1)
        Pipes[-1].append('.')
        Pipes[-1].append(x)
    Pipes[-1].append('.')
    i += 1
Pipes.append(Pipes[0])

Pipes = np.asarray(Pipes)

for i, row in enumerate(Pipes):
    if i % 2 == 0:
        continue
    for j, pipe in enumerate(row):
        if j % 2 == 0:
            continue
        if pipe in pieces:
            for offset in pieces[pipe]:
                if np.array_equal(offset, UP) or np.array_equal(offset, DOWN):
                    Pipes[addTuples((i, j), offset)] = '|'
                elif np.array_equal(offset, LEFT) or np.array_equal(offset, RIGHT):
                    Pipes[addTuples((i, j), offset)] = '-'
                else:
                    raise()

for sub in ['|', '-', 'L', 'J', '7', 'F']:
    BoolPipes = np.zeros(Pipes.shape)
    pos = start_pos
    Pipes[pos] = sub
    BoolPipes[pos] = 1
    step = pieces[Pipes[pos]][0]
    steps_taken = 1
    BoolPipes[pos] = steps_taken
    pos = addTuples(pos, step)
    while True:
        steps_taken += 1
        neg_step = negTuple(step)
        BoolPipes[pos] = 1
        try: 
            path_taken = pieces[Pipes[pos]].index(neg_step)
        except:
            steps_taken = -1
            break
        
        if np.array_equal(pos, start_pos):
            print("Starting spread...")

            def spread(pos):
                spread_positions = [pos]
                BoolPipes[pos] = -1
                while len(spread_positions) > 0:
                    curr_pos = spread_positions[0]
                    for _, dir in directions.items():
                        new_pos = addTuples(curr_pos, dir)
                        if 0 <= new_pos[0] < BoolPipes.shape[0] and 0 <= new_pos[1] < BoolPipes.shape[1]:
                            if BoolPipes[new_pos] == 0:
                                BoolPipes[new_pos] = -1
                                spread_positions.append(new_pos)
                    spread_positions = spread_positions[1:]

            spread((0                   , 0                   ))
            spread((BoolPipes.shape[0]-1, 0                   ))
            spread((0                   , BoolPipes.shape[1]-1))
            spread((BoolPipes.shape[0]-1, BoolPipes.shape[1]-1))
            count = 0
            for i, row in enumerate(BoolPipes):
                if i % 2 == 0:
                    continue
                for j, pipe in enumerate(row):
                    if j % 2 == 0:
                        continue
                    if pipe == 0:
                        print("I", end="")
                        count += 1
                    else:
                        print(" ", end="")
                print()
            print("\nWorking pipe:", sub, "Steps taken:", steps_taken // 2, "Enclosures:", count)
            exit()

        step = pieces[Pipes[pos]][(path_taken + 1) % 2]
        pos = addTuples(pos, step)
