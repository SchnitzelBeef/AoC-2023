
def findFirstNumber(str, amp, dic):
    first = len(str)
    for number, digit in enumerate(dic):
        index = str.find(digit)
        if (index != -1 and index <= first):
            first = index
            dig = number+1
    for i, chr in enumerate(str):
        if chr.isdigit():
            if i < first:
                return int(chr) * amp
            break
    return dig * amp

sum = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

while (line := input()) != "":
    sum += findFirstNumber(line, 10, digits)
    sum += findFirstNumber(line[::-1], 1, [digit[::-1] for digit in digits])
print(sum)
