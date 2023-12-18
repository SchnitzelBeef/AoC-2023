
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
energized_grid = np.full(shape=(grid.shape[0], grid.shape[1], 4), dtype=bool, fill_value=False)
energized_total = np.zeros(shape=grid.shape)

def follow_light(pos : (int, int), d : int):
    curr_positions = [(pos, d)]
    while len(curr_positions) > 0:
        pos, d = curr_positions.pop(0)
        dir = Directions[d]
        new_pos = addTuples(pos, dir)
        if 0 <= new_pos[0] < grid.shape[0] and 0 <= new_pos[1] < grid.shape[1]:
            
            # Check if path is already traversed before:
            if energized_grid[new_pos[0], new_pos[1], d]:
                continue
            
            energized_total[new_pos] += 1
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
        
pos0 = (0, 0)
energized_total[pos0] = 1
dir = 0
match grid[pos0]:
    case '|':
        follow_light(pos0, 1) # Down
    case ')':
        follow_light(pos0, 1) # Down
    case '/':
        follow_light(pos0, 3) # Up
    case _ :
        follow_light(pos0, 0)


res = open("temp.txt", "w")
res.write(np.array2string(energized_total, max_line_width=sys.maxsize, threshold=sys.maxsize))

n_energized = 0
for elm in np.nditer(energized_total):
    if elm != 0:
        n_energized += 1

print("Energized cells:", n_energized)