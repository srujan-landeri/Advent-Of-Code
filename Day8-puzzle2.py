with open('./calibratoion document[d8p2].txt', 'r') as f:
    data = f.readlines()

    directions = data[0]
    source = 'AAA'

with open('./calibratoion document[d8p2].txt', 'r') as f:
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


sources = []

for node in nodes:
    if node.endswith("A"):
        sources.append(node)

print(sources)

# source = '22A'
# while not found:
#     source = nodes[source][getInd(directions[ind % len(directions)])].strip()
#     ind += 1
#     if source.endswith('Z'):
#         found = True
#     steps+=1

# print(steps)

allSteps = []

for s in range(len(sources)):
    source = sources[s]
    print(source)   
    steps = 0 
    found = False
    while not found:
        source = nodes[source][getInd(directions[ind % len(directions)])].strip()
        ind += 1
        if source.endswith('Z'):
            found = True
        steps+=1

    allSteps.append(steps)

from math import lcm

print(lcm(*allSteps))