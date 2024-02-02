import re

def noStars(row,ss,ee):
    for i in range(ss,ee):
        if lines[row][0][i] == "*":
            return False
    return True


def check(row, line):
    ind = 0
    line = line[0]

    while ind < len(line):
        ss = -1
        ee = -1

        if line[ind].isdigit():

            ss = ind
            ee = ind

            while ind < len(line) and line[ind].isdigit():
                ee += 1
                ind += 1

            print("Number: ", ss, ee)
            sss = max(0, ss-1)
            eee = min(len(line) - 1, ee + 1)
            
            up = max(0, row - 1)
            down = min(len(lines) - 1, row + 1)

            # horizontal
            if(noStars(row, sss,eee+1)):
                for i in range(ss, ee):
                    lines[row][0][i] = " "

            # up
            if(noStars(up, sss,eee+1)):
                for i in range(ss, ee):
                    lines[up][0][i] = " "

            # down
            if(noStars(down, sss,eee+1)):
                for i in range(ss, ee):
                    lines[down][0][i] = " "

        ind += 1

update_lines = []
lines = None

# Read the file and process the lines
with open('./calibration document [d3p2].txt', 'r') as f:
    for line in f:
        update_line = re.sub(r'[^0-9*]', ' ', line)
        update_lines.append([update_line])
    
    lines = update_lines

for i in range(len(update_lines)):
    check(i, lines[i])
    break