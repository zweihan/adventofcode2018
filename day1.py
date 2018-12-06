
def part1():
    with open("day1_input.txt", 'r') as f:
        count = 0
        for i in f:
            inti = int(i)
            count+=inti
        print(count)

def part2():
     with open("day1_input.txt", 'r') as f:
        count = 0
        intdict= dict()
        intarr = []
        for i in f:
            inti = int(i)
            intarr.append(inti)
        shouldrepeat = True
        while(shouldrepeat):
            for i in intarr:
                count += i
                if count in intdict:
                    print(count)
                    shouldrepeat = False
                    break
                else:
                    intdict[count] = 1
# part1()
part2()