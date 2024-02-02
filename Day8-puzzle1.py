with open('./calibaration document[d8p1].txt', 'r') as f:
    data = f.readlines()

    directions = data[0]
    source = 'AAA'

with open('./calibaration document[d8p1].txt', 'r') as f:
    lines = []

    for line in f:
        if '=' not in line:
            pass

        else:
            lines.append(line)

    nodes = {

    }

    for line in lines:
        k, v = line.split('=')
        k = k.strip()
        v = v.strip()[1:-1]
        nodes[k] = v.split(',')


def getInd(dir):
    if dir == 'L':
        return 0
    else:
        return 1
    
steps = 0
found = False
ind = 0
directions = directions.strip()

while not found:
    source = nodes[source][getInd(directions[ind % len(directions)])].strip()
    ind += 1
    print(source)
    if source == 'ZZZ':
        found = True
    steps+=1



print(steps)
