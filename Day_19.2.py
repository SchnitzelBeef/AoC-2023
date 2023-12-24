
print("DAY 19.2 AoC 2023\n---------------------------")

Workflows = {}

while (line := input()) != "":
    name, rules = line[:-1].split("{")
    rules = rules.split(",") 
    Workflows[name] = []
    for rule in rules[:-1]:
        cond, dest = rule.split(":")
        variable, sign, value = cond[0], cond[1], int(cond[2:])
        match sign:
            case "<": 
                Workflows[name].append((variable, (value, False), dest))
            case ">":
                Workflows[name].append((variable, (value, True), dest))
            case _ :
                raise("Unrecognized symbol in condition")
    Workflows[name].append(rules[-1])

while (line := input()) != "":
    pass

RangesSet = [("in", {
    "x" : (1, 4000),
    "m" : (1, 4000),
    "a" : (1, 4000),
    "s" : (1, 4000)
})]

n = 0
while len(RangesSet) > 0:
    currName, currRange = RangesSet.pop(0)        
    
    if currName == "A":
        a = 1
        for _, range in currRange.items():
            a *= (range[1] - range[0] + 1)
        n += a
        continue

    if currName == "R":
        continue
        
    for (variable, (v, bigger), dest) in Workflows[currName][:-1]:         
        if currRange[variable][0] <= v <= currRange[variable][1]:
            newRange = currRange.copy()
            if bigger:
                newRange[variable] = (v+1, currRange[variable][1])
                currRange[variable] = (currRange[variable][0], v)
            else:
                newRange[variable] = (currRange[variable][0], v-1)
                currRange[variable] = (v, currRange[variable][1])
            RangesSet.append((dest, newRange))
    else:
        RangesSet.append((Workflows[currName][-1], currRange))
                
print("Result:", n)