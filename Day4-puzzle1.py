def getCount(line):
    processed = line.split(':')[1]
    processed = processed.split('|')
    win = set(processed[0].split())
    mine = set(processed[1].split())
    res = (win.intersection(mine))
    if len(res) != 0:
        return pow(2,len(res) - 1)
    else:
        return 0

sum = 0
with open('./calibration document [d4p1].txt', 'r') as f:
    for line in f:
        sum += getCount(line)

print(sum)