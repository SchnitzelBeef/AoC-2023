
import numpy as np

print("DAY 13.2 AoC 2023\n---------------------------")

def findSplit(mirror):
    def compareRow(A, B):
        error = False
        for i, (a, b) in enumerate(zip(A, B)):
            if a != b:
                if error:
                    return 2
                error = True
        return error
    
    def runThroughMirror(sub_mirror, mul):
        for i in range(len(sub_mirror)-1):
            j = 0
            errors = 0
            while errors < 2:
                errors += compareRow(sub_mirror[i-j], sub_mirror[i+1+j])
                j+=1
                if i - j < 0 or i + 1 + j > len(sub_mirror)-1:
                    if errors == 1:
                        return (i+1)*mul
                    else:
                        break

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
    
print("Result:", sum)
