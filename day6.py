from collections import namedtuple
class loc:
    def __init__(self, id,x,y):
        self.id = id
        self.x = x
        self.y = y
        self.count=0
class point:
    def __init__(self, loc, steps):
        self.loc = loc
        self.steps = steps
def part1():
    with open("day6_input.txt", 'r') as f:
        locs = []
        count = 1
        for line in f:
            x = int(line.split(", ")[0].strip())
            y = int(line.split(", ")[1].strip())
            locs.append(loc(id=str(count),x=x,y=y))
            count+=1
        print(locs)        
        points =[]
        for i in range(0, 400):
            points.append([])
            for j in range(0,400):
                points[i].append(point(loc="-1", steps = -1))
        for loca in locs:
            pt = points[loca.x][loca.y]
            pt.loc = loca.id
            pt.steps = 0
        for i in range(1, 400):
            perms = generateperms(i)
            for loca in locs:
                for perm in perms:
                    if loca.x+perm[0] >= 0 and loca.y+perm[1] >= 0 and loca.x+perm[0] < 400 and loca.y+perm[1] < 400:
                        pt = points[loca.x+perm[0]][loca.y+perm[1]]
                        if pt.loc == "-1":
                            pt.loc = loca.id
                            pt.steps = i
                        elif pt.steps > i:
                            pt.loc = loca.id
                            pt.steps = i
                        elif pt.steps == i:
                            pt.loc = "."
        locdict = dict()
        for loca in locs:
            locdict[loca.id] = loca
        for i in range(0,400):
            for j in range(0, 400):
                pt = points[i][j]
                if pt.loc == "-1":
                    print("hey! %d,%d"%(i,j))
                if pt.loc != "." and pt.loc != "-1":
                    loca = locdict[pt.loc]
                    loca.count += 1
        eliminatedlocas = dict()
        for i in range(0,400):
            pt = points[0][i]
            if pt.loc not in eliminatedlocas.keys():
                eliminatedlocas[pt.loc] = True
            pt = points[399][i]
            if pt.loc not in eliminatedlocas.keys():
                eliminatedlocas[pt.loc] = True
            pt = points[i][0]
            if pt.loc not in eliminatedlocas.keys():
                eliminatedlocas[pt.loc] = True
            pt = points[i][399]
            if pt.loc not in eliminatedlocas.keys():
                eliminatedlocas[pt.loc] = True
        for loca in locs:
            if loca.id not in eliminatedlocas.keys():
                print("id: %s, coord: %d, %d, count: %d"%(loca.id, loca.x,loca.y, loca.count))
def generateperms(n):
    perms = []
    perms.append((0,n))
    perms.append((0,-n))
    perms.append((n,0))
    perms.append((-n,0))
    for i in range(1,n):
        perms.append((i,n-i))
        perms.append((-i,-(n-i)))
        perms.append((-i,n-i))
        perms.append((i, -(n-i)))
    return perms


def part2():
    
    with open("day6_input.txt", 'r') as f:
        locs = []
        count = 1
        for line in f:
            x = int(line.split(", ")[0].strip())
            y = int(line.split(", ")[1].strip())
            locs.append(loc(id=str(count),x=x,y=y))
            count+=1
        points =[]
        count = 0     
        for i in range(0, 1000):
            for j in range(0,1000):
                dist = 0
                for loca in locs:
                    dist += abs(i-loca.x) + abs(j-loca.y)
                if dist < 10000:
                    count+=1
        print(count)
# part1()
part2()