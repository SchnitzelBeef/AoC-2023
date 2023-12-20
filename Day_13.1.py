
import numpy as np

print("DAY 13.1 AoC 2023\n---------------------------")

def findSplit(mirror):    
    def runThroughMirror(sub_mirror, mul):
        for i in range(len(sub_mirror)-1):
            j = 0
            while  np.array_equal(sub_mirror[i-j], sub_mirror[i+1+j]):
                j+=1
                if i - j < 0 or i + 1 + j > len(sub_mirror)-1:
                    return (i+1)*mul
        return None
    
    return runThroughMirror(mirror, 100) or runThroughMirror(np.rot90(mirror, 3), 1)
    

mirror = []
sum = 0
while True:
    line = input()
    if line == "":
        sum += findSplit(mirror)
        mirror = []
        line = input()
        if line == "":
            break
    mirror.append(list(line))
    
print("Result:",sum)
