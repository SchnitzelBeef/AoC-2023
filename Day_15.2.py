
import sys

print("DAY 15.2 AoC 2023\n---------------------------")

if len(sys.argv) == 2:
    steps = sys.argv[1].split(',')
    print("READING FROM COMMAND LINE.")
else:
    f = open("day_15_input.txt", "r")
    steps = f.read().rstrip().split(',')
    print("READING FROM TEXT FILE.")

Boxes = {}

for step in steps:
    step_sum = 0
    item = ""
    for i, c in enumerate(step):
        match c:
            case '-':
                if step_sum in Boxes and item in Boxes[step_sum]:
                    del Boxes[step_sum][item]
                    if Boxes[step_sum] == {}:
                        del Boxes[step_sum]
            case '=':
                if step_sum not in Boxes:
                    Boxes[step_sum] = {}
                Boxes[step_sum][item] = int(step[i+1])
            case _:
                item += c      
        step_sum = ((step_sum + ord(c)) * 17) % 256

focusing_power = 0

for nr, Box in Boxes.items():
    for i, (_, focal_length) in enumerate(Box.items()):
        focusing_power += (nr + 1) * (i + 1) * focal_length   

print("Resulting focusing power", focusing_power)