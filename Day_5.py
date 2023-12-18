
import sys

DRS = 0
SRS = 1
RL = 2

map_table = []

data = [int(s) for s in input().split(' ')[1:]]
seeds = []


def run_through_map(seed_x0, seed_x1, i = 0):
    if i == len(map_table):
        # print("Returns: ", seed_x0)
        return seed_x0

    for sub_table in map_table[i]:
        # print("sub-table:", sub_table, "seeds:", [seed_x0, seed_x1])
        map_x0 = sub_table[SRS]
        map_x1 = sub_table[SRS] + sub_table[RL]
        dest_offset = sub_table[DRS]-sub_table[SRS]

        if seed_x0 <= map_x0 and seed_x1 >= map_x1:
            # print("Seeds covers map")
            return min(run_through_map(seed_x0, map_x0-1, i+1),
                run_through_map(map_x0+dest_offset, map_x1+dest_offset-1, i+1),
                run_through_map(map_x1, seed_x1, i+1))
        # In between: 
        if  seed_x0 >= map_x0 and seed_x1 <= map_x1:
            # print("Seed is in between map")
            return run_through_map(seed_x0+dest_offset, seed_x1+dest_offset, i+1)
        # Overlaps start:
        elif seed_x0 >= map_x0 and seed_x0 <= map_x1:
            # print("Map overlaps start of seeds")
            return min(run_through_map(seed_x0+dest_offset, map_x1+dest_offset-1, i+1),
               run_through_map(map_x1, seed_x1, i+1))
        # Overlaps end:
        elif seed_x1 >= map_x0 and seed_x1 <= map_x1:
            # print("Map overlaps end of seeds")
            return min(run_through_map(seed_x0, map_x0-1, i+1),
                run_through_map(map_x0+dest_offset, seed_x1+dest_offset, i+1))
    
    # print("NO",seed_x0, seed_x1)
    return run_through_map(seed_x0, seed_x1, i+1)
    

for i in range(0, len(data)-1, 2):
    seeds.append([data[i], data[i]+data[i+1]])
    
input()
try:
    while (line := input()) != "":
        map_table.append([])
        while (line := input()) != "":
            map_table[-1].append([int(t) for t in line.split(' ')])
            if line == "end":
                raise()
except:
    pass

global_min = sys.maxsize

print("\nCalculating...")
for seed in seeds:
    value = run_through_map(seed[0], seed[1])
    print("Seed:", seed, value)
    global_min = min(value, global_min)

print(global_min)
