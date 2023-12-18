
import numpy as np

stars = []
star_positions = []

while (line := input()) != "":
    row = []
    empty = True
    for x in line:
        if x == '#':
            empty = False
        row.append(x)
    stars.append(row)
    if empty:
        stars.append(row)

stars = np.asarray(stars)
stars = np.rot90(stars)

expanded_stars = []

for i, row in enumerate(stars):
    empty = True
    for x in row:
        if x == '#':
            break
    else:
        expanded_stars.append(row)
    expanded_stars.append(row)
    
        
expanded_stars = np.rot90(np.asarray(expanded_stars), 3)

star_positions = []

for i, row in enumerate(expanded_stars):
    for j, elm in enumerate(row):
        if elm == '#':
            star_positions.append((i, j))

total_dist = 0

for i, pos1 in enumerate(star_positions):
    for pos2 in star_positions[i:]:
        total_dist += abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

print(total_dist)
