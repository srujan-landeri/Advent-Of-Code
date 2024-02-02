sum = 0;

def getNum(line):
    ind = 0

    while not line[ind].isdigit() :
        ind += 1

    n1 = line[ind]

    ind = len(line) - 1

    while not line[ind].isdigit() :
        ind -= 1

    n2 = line[ind]

    return int(n1 + n2)



with open('./calibration document [d1p1].txt', 'r') as f:
    for line in f:
        sum += getNum(line)
    
    print(sum)

