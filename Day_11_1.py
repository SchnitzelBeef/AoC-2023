
import numpy as np

stars, star_positions, expansionsYAxis, expansionsXAxis = [], [], [], []

i = 0
while (line := input()) != "":
    row = []
    empty = True
    for j, x in enumerate(line):
        if x == '#':
            empty = False
        row.append(x)
    stars.append(row)
    if empty:
        expansionsYAxis.append(i)
    i += 1

stars = np.asarray(stars)
stars = np.rot90(stars, 3)

for i, row in enumerate(stars):
    empty = True
    for x in row:
        if x == '#':
            empty = False
    if empty:
        expansionsXAxis.append(i)

stars = np.rot90(np.asarray(stars), 1)

star_positions = []

for i, row in enumerate(stars):
    for j, elm in enumerate(row):
        if elm == '#':
            star_positions.append((i, j))

EXPANSION_SIZE = 1000000
if (EXPANSION_SIZE <= 1):
    EXPANSION_SIZE = 2
total_dist = 0

for i, pos1 in enumerate(star_positions):
    for pos2 in star_positions[i+1:]:
        minX, maxX = sorted([pos1[1], pos2[1]])
        minY, maxY = sorted([pos1[0], pos2[0]])
        for eXx in expansionsXAxis:
            if minX < eXx < maxX:
                total_dist += EXPANSION_SIZE-1
        for eXy in expansionsYAxis:
            if minY < eXy < maxY:
                total_dist += EXPANSION_SIZE-1
        total_dist += maxX - minX + maxY - minY

print(total_dist)
