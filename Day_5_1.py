
import sys

DRS = 0
SRS = 1
RL = 2

map_table = []

data = [int(s) for s in input().split(' ')[1:]]


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

min_seed_value = sys.maxsize
for i in range(0, len(data), 2):
    print("Set", (i+2),"/",len(data), "of seeds started")
    seeds = []
    for seed_value in range(data[i], data[i]+data[i+1]):
        for table in map_table:
            for sub_table in table:
                if seed_value >= sub_table[SRS] and seed_value < sub_table[SRS] + sub_table[RL]:
                    seed_value =  sub_table[DRS] + seed_value - sub_table[SRS]
                    break

        min_seed_value = min(min_seed_value, seed_value) 

print(min_seed_value)
