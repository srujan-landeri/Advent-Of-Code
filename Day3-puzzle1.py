def check(row, line, lines):
    ind = 0
    num = []
    sum = 0
    s = -1
    e = -1
    print()
    # print(line)

    while ind != len(line):
        if(line[ind].isdigit()):
            s = ind
            e = s
            while ind != len(line) and line[ind].isdigit():
                e += 1
                ind += 1
        else:
            ind+=1

        if s != -1:
            li = [s , e - 1]
            num.append(li)

            s = -1
            e = -1

    for number in num:
        
        s = number[0]
        e = number[1]

        # horizontal symbol check
        ss = max(s - 1, 0)
        ee = min(len(line)-1, e + 1)
        print("checking: ", line[s:e+1], ss, ee, row)
        
        if hasSymbol(line, ss, ee):
            print(line[s:e+1])
            sum += int(line[s:e+1])
            continue

        # checking symbol up
        row_num = max(0, row - 1)
        ss = max(s - 1, 0)
        ee = min(len(line)-1, e + 1)
        print("checking: ", line[s:e+1], ss, ee, row_num)
        
        if hasSymbol(lines[row_num], ss, ee):
            print(line[s:e+1])
            sum += int(line[s:e+1])
            continue
        
        # checking symbol down
        row_num = min(len(lines[row]) - 1, row + 1);
        ss = max(s - 1, 0)
        ee = min(len(line)-1, e + 1)
        print("checking: ", line[s:e+1], ss, ee, row_num)

        if hasSymbol(lines[row_num], ss, ee):
            print(line[s:e+1])
            sum += int(line[s:e+1])
            continue

    return sum

def hasSymbol(line, start, end):
    for i in range(start, end + 1):
        if not line[i].isdigit() and  line[i] != '.':
            return True
    
    return False
sum = 0  

with open('./calibration document [d3p1].txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        sum += check(i, lines[i].replace('\n', ''),lines)

print('\n', sum)