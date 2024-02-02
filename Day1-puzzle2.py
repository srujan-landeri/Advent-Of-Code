list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def getDigit(line):
    minimum = len(line)
    firstNum = ""

    maximum = -1
    lastNum = ""

    for d in list:
        try:
            # first occurence
            if(line.index(d) < minimum):
                minimum = line.index(d)
                firstNum = d

            # last occurence
            if(line.rfind(d) > maximum):
                maximum = line.rfind(d)
                lastNum = d

        except ValueError:
            pass 

    if(not firstNum.isdigit()):
        firstNum = mapWord(firstNum)
        
    if(not lastNum.isdigit()):
        lastNum = mapWord(lastNum)

    return int(firstNum + lastNum)

    
def mapWord(word):
    if word == 'one': 
        return "1"
    if word == 'two': 
        return "2"
    if word == 'three': 
        return "3"
    if word == 'four': 
        return "4"
    if word == 'five': 
        return "5"
    if word == 'six': 
        return "6"
    if word == 'seven': 
        return "7"
    if word == 'eight': 
        return "8"
    if word == 'nine': 
        return "9"
    if word == 'zero': 
        return "0"
    
sum = 0

with open('./calibration document [d1p2].txt', 'r') as f:
    for line in f:
        sum += getDigit(line)

    print(sum)

