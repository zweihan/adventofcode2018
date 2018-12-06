import time

def part1():
    with open("day5_input.txt", 'r') as f:
        line = f.readline()
        print(len(line))
        st1 = time.time()
        div = divideline(line)
        st2 = time.time()

        red = reduceline(line)
        st3 = time.time()
        divt = st2-st1
        redt = st3-st2
        print(divt)
        print(redt)
        print("div: %d, red: %d"%(len(div), len(red)))


def divideline(line):
    linelen = len(line)
    # print(linelen)
    if linelen > 12000:
        midpoint = round(linelen/2)
        # print(line[:midpoint])
        newline = divideline(line[:midpoint]) + divideline(line[midpoint:])
        return divideline(newline)
    else:
        return reduceline(line)

def reduceline(line):
    linelenbef = 0
    linelenaft = len(line)
    while linelenbef != linelenaft:
        linelenbef = len(line)
        # print("bef: %d, aft: %d, line: %s"%(linelenbef, linelenaft, line))
        for i in range(0,linelenaft):
            if i+1 >= len(line):
                break
            if line[i].upper() == line[i+1].upper() and line[i] != line[i+1]:
                if i == 0:
                    line = line[2:]
                elif i+2 < len(line):
                    line = line[:i] + line[i+2:]
                else:
                    line = line[:i]
                linelenaft = len(line)
                break
            linelenaft = len(line)
    return line

def part2():
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    with open("day5_input.txt", 'r') as f:
        line = f.readline()
        shortest = -1
        shortestchar = ''
        for char in chars:
            newline = line.replace(char,'').replace(char.upper(),'')
            div = divideline(newline)
            if shortest < 0 or len(div) < shortest:
                shortest = len(div)
                shortestchar = char
            print(len(div))
            print(char)
        print("\n\n")
        print(shortest)
        print(shortestchar)


part2()