sum = 0

red = 12
green = 13
blue = 14

def getConfig(color):
    if color == "red":
        return 12
    
    if color == "green":
        return 13 
    
    if color == "blue":
        return 14
    
def isPossible(line):


    ind = line.index(':')
    main = line[ind + 1:]
    
    #! write code for id...
    
    sets = main.split(';')

    blue = 0
    green = 0
    red = 0

    for set in sets:
        colors = set.split(',')
        for color in colors:
            num, givenColor = color.split(' ')[1:]
            
            if "green" in givenColor:
                if getConfig("green") < num:
                    return 0

            if "red" in givenColor:
                if getConfig("red") < num:
                    return 0

            if "blue" in givenColor:
                if getConfig("blue") < num:
                    return 0
    
    return id

        

with open('./calibration document [d2p1].txt', 'r') as f:
    for line in f:
        sum += isPossible(line)
    print(sum)