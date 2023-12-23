
print("DAY 19.1 AoC 2023\n---------------------------")

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
                Workflows[name].append((variable, lambda y, v=value : y < v, dest))
            case ">":
                Workflows[name].append((variable, lambda y, v=value : y > v, dest))
            case _ :
                raise("Unrecognized symbol in condition")
    Workflows[name].append(rules[-1])

total = 0
while (line := input()) != "":
    currentFlow = {}
    ratings = line[1:-1].split(",")
    for rating in ratings:
        name, value = rating.split("=")
        currentFlow[name] = int(value)
        
    name = "in"
    while name != "A" and name != "R":
        for (variable, func, dest) in Workflows[name][:-1]:                  
            if func(int(currentFlow[variable])):
                name = dest
                break
        else:
            name = Workflows[name][-1]
    
    if name == "A":
        total += sum(currentFlow.values())
                
print("Result:", total)