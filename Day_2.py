
power = 0

ball_set = {
    "red": 0,
    "green": 0,
    "blue": 0
}

while (line := input()) != "":
    for ball in ball_set:
        ball_set[ball] = 0
        
    data = line.split(":")[1]
    for round in data.split(";"):
        for ball in round.split(","):
            n, col = ball.split()
            if (int(n) > ball_set[col]):
                ball_set[col] = int(n)
    
    power += ball_set["red"] * ball_set["green"] * ball_set["blue"]
        
print(power)
