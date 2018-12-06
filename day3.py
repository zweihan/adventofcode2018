
from collections import namedtuple
Cloth = namedtuple("Cloth", ["id","x", "y", "xlen", "ylen"])

def part1():
    with open("day3_input.txt", 'r') as f:
        cloths = []
        for line in f:
            cid = line.split("@")[0].strip()
            useful = line.split("@")[1].strip().split(":")
            xy = useful[0].split(",")
            lens = useful[1].split("x")
          
            cloth = Cloth(id = cid,x=int(xy[0]), y=int(xy[1]), xlen = int(lens[0]), ylen = int(lens[1]))            
            cloths.append(cloth)

        clothmap = [ [ None for y in range( 1000 ) ] for x in range( 1000 ) ]
        count = 0
        for cloth in cloths:
            for x in range(cloth.x, cloth.x+cloth.xlen):
                for y in range(cloth.y, cloth.y+cloth.ylen):
                    if clothmap[x][y] is None:
                        clothmap[x][y] = 1
                    elif clothmap[x][y] == 1:
                        clothmap[x][y] = 2
                        count+=1
        print(count)



def part2():
     with open("day3_input.txt", 'r') as f:
        cloths = []
        for line in f:
            cid = line.split("@")[0].strip()
            useful = line.split("@")[1].strip().split(":")
            xy = useful[0].split(",")
            lens = useful[1].split("x")
          
            cloth = Cloth(id = cid,x=int(xy[0]), y=int(xy[1]), xlen = int(lens[0]), ylen = int(lens[1]))            
            cloths.append(cloth)

        clothmap = [ [ None for y in range( 1000 ) ] for x in range( 1000 ) ]
        for cloth in cloths:
            for x in range(cloth.x, cloth.x+cloth.xlen):
                for y in range(cloth.y, cloth.y+cloth.ylen):
                    if clothmap[x][y] is None:
                        clothmap[x][y] = 1
                    elif clothmap[x][y] == 1:
                        clothmap[x][y] = 2
        for cloth in cloths:
            hasOverlap = False
            for x in range(cloth.x, cloth.x+cloth.xlen):
                for y in range(cloth.y, cloth.y+cloth.ylen):
                    if clothmap[x][y] > 1:
                        hasOverlap = True
            if hasOverlap == False:
                print(cloth.id)
part2()