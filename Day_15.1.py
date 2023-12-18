
import sys

print("DAY 15.1 AoC 2023\n---------------------------")

if len(sys.argv) == 2:
    steps = sys.argv[1].split(',')
    print("READING FROM COMMAND LINE.")
else:
    f = open("day_15_input.txt", "r")
    steps = f.read().rstrip().split(',')
    print("READING FROM TEXT FILE.")


hash_sum = 0
for step in steps:
    step_sum = 0
    for c in step:
        step_sum = ((step_sum + ord(c)) * 17) % 256
    hash_sum += step_sum

print(hash_sum)
