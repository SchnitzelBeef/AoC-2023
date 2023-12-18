
import numpy as np
import sys

Directions = {
    0: (0, 1),  # RIGHT
    1: (1, 0),  # DOWN
    2: (0, -1), # LEFT
    3: (-1, 0), # UP
}

def addTuples(X : (int, int), Y : (int, int)):
    return (X[0] + Y[0], X[1] + Y[1])

print("DAY 16.1 AoC 2023\n---------------------------")

# To load data properly, all '\' needs to be replaced with ')'
f = open("day_16_input.txt", "r")

grid = []

for line in f.readlines():
    grid.append(list(line.rstrip()))

grid = np.asarray(grid)

def follow_light(pos : (int, int), d : int):
    energized_grid = np.full(shape=(grid.shape[0], grid.shape[1], 4), dtype=bool, fill_value=False)
    energized_total = np.zeros(shape=grid.shape)
    
    def switchWay(p, d):
        if d % 2: # Down or Up
            match grid[p]:
                case '-':
                    curr_positions.append((p, 0))
                    curr_positions.append((p, 2))
                case ')':
                    curr_positions.append((p, (d-1) % 4))
                case '/':
                    curr_positions.append((p, (d+1) % 4))
                case _ :
                    curr_positions.append((p, d))
        else: # Left or Right
            match grid[p]:
                case '|':
                    curr_positions.append((p, 1))
                    curr_positions.append((p, 3))
                case ')':
                    curr_positions.append((p, (d+1) % 4))
                case '/':
                    curr_positions.append((p, (d-1) % 4))
                case _ :
                    curr_positions.append((p, d))
    
    curr_positions = []
    switchWay(pos, d)
    energized_total[pos] = 1
    
    while len(curr_positions) > 0:
        pos, d = curr_positions.pop(0)
        dir = Directions[d]
        new_pos = addTuples(pos, dir)
        if 0 <= new_pos[0] < grid.shape[0] and 0 <= new_pos[1] < grid.shape[1]:
            
            # Check if path is already traversed before:
            if energized_grid[new_pos[0], new_pos[1], d]:
                continue
            
            energized_total[new_pos] = 1
            energized_grid[new_pos[0], new_pos[1], d] = True

            if d % 2: # Down or Up
                match grid[new_pos]:
                    case '-':
                        curr_positions.append((new_pos, 0))
                        curr_positions.append((new_pos, 2))
                    case ')':
                        curr_positions.append((new_pos, (d-1) % 4))
                    case '/':
                        curr_positions.append((new_pos, (d+1) % 4))
                    case _ :
                        curr_positions.append((new_pos, d))
            else: # Left or Right
                match grid[new_pos]:
                    case '|':
                        curr_positions.append((new_pos, 1))
                        curr_positions.append((new_pos, 3))
                    case ')':
                        curr_positions.append((new_pos, (d+1) % 4))
                    case '/':
                        curr_positions.append((new_pos, (d-1) % 4))
                    case _ :
                        curr_positions.append((new_pos, d))
    
    n_energized = 0
    for elm in np.nditer(energized_total):
        n_energized += elm 

    return n_energized
    
best = 0
for i in range(grid.shape[1]-1):
    best = max(best, follow_light(addTuples((0,0), (0, i)), 1)) # Down
    best = max(best, follow_light(addTuples((grid.shape[0]-1,0), (0, i)), 3)) # Up

for i in range(grid.shape[0]-1):
    best = max(best, follow_light(addTuples((0,0), (i, 0)), 0)) # Right
    best = max(best, follow_light(addTuples((0,grid.shape[1]-1), (i, 0)), 2)) # Left

print("Energized cells:", int(best))