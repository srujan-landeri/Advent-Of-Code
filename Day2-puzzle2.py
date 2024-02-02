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
    
    # need to find ID

    main = line[ind + 1:]
    
    sets = main.split(';')

    blue = 0
    green = 0
    red = 0

    for set in sets:
        colors = set.split(',')
        for color in colors:
            num, givenColor = color.split(' ')[1:]
            
            if "green" in givenColor:
                green = max(int(num), green)

            if "red" in givenColor:
                red = max(int(num) , red)

            if "blue" in givenColor:
                blue = max(int(num), blue)
    
    return green * red * blue

        

with open('./calibration document [d2p2].txt', 'r') as f:
    for line in f:
        sum += isPossible(line)
    print(sum)