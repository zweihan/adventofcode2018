def part1():
    with open("day2_input.txt", 'r') as f:
        count2 = 0
        count3 = 0
        for line in f:
            chardict = dict()
            for char in line:
                if char in chardict:
                    chardict[char] += 1
                else:
                    chardict[char] = 1
            count2already = False
            count3already = False
            for char in chardict.keys():
                if not count2already and chardict[char] == 2:
                    count2+=1
                    count2already = True
                if not count3already and chardict[char] == 3:
                    count3+=1
                    count3already = True
                if count2already and count3already:
                    break
        print(count2)
        print(count3)
        print(count2*count3)


def differbyone(a,b):
    diffCount = 0
    length = len(a)
    for i in range(0, length):
        if a[i] == b[i]:
            continue
        else:
            diffCount+=1
    return diffCount <= 1
def printsame(a,b):
    newline = ""
    length = len(a)
    for i in range(0, length):
        if a[i] == b[i]:
            newline +=a[i]
    return newline
def part2():
    with open("day2_input.txt", 'r') as f:
        lines = []
        for line in f:
            lines.append(line)
        totallen = len(lines)
        ansa = -1
        ansb = -1
        for i in range(0, totallen):
            for j in range(0, totallen):

                if i != j and  differbyone(lines[i], lines[j]):
                    ansa = i
                    ansb = j
                    break
        print(ansa)
        print(ansb)
        print(lines[ansa])
        print(lines[ansb])
        print(printsame(lines[ansa],lines[ansb]))



part2()

