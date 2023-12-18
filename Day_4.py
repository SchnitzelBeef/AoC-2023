
sum = 0

total_cards = []

total_games = []

while (line := input()) != "":

    card = line.split(':')[1]
    winnings, numbers = card.split('|')
    winnings = winnings.split(" ")
    numbers = numbers.split(" ")

    count = 0    

    for winning in winnings:
        if winning == '':
            count += 1            

    while count > 0:
        winnings.remove('')
        count -= 1

    total_cards.append(1)
    total_games.append((winnings, numbers))

sum = 0

for i, (winnings, numbers) in enumerate(total_games):
    j = 0

    for number in numbers:
        if number in winnings:
            j += 1 
            total_cards[i+j] += 1*total_cards[i]
    
    sum += total_cards[i]

print(sum)
