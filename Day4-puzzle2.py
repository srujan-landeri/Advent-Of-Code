map = {

}

def getCount(line):
    processed = line.split(':')
    id = processed[0].split()[1]
    processed = processed[1]
    processed = processed.split('|')
    win = set(processed[0].split())
    mine = set(processed[1].split())
    res = (win.intersection(mine))
    
    id = int(id)

    print(id, len(res))

    if(map.get(id) == None):
        map[id] = 1
    else:
        map[id] += 1
    
    n = map[id]

    while n:
        for i in range(id + 1, id + len(res) + 1):
            if(map.get(i) == None):
                map[i] = 1
            else:
                map[i] += 1
        n -= 1

sum = 0

with open('./calibration document [d4p2].txt', 'r') as f:
    lines = (f.readlines())
    for line in lines:
        getCount(line)

    for v in map.values():
        sum += v

print(map)
print(sum)