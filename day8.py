class Node:
    def __init__(self, numChildren, numMeta):
        self.cCount = numChildren
        self.mCount = numMeta
        self.children = []
        self.metadata = []


def readinput():
    ilist = []
    f = open("day8_input.txt", 'r')
    for line in f:
        ilist = [int(x) for x in line.split(" ")]
    return ilist
def part1():
    ilist = readinput()
    node, cidx = createnode(ilist,0)
    print(len(ilist))
    print(cidx)
    print(summeta(node))

def part2():
    ilist = readinput()
    node, cidx = createnode(ilist,0)
    printnode(node)
    print(calcnodeval(node))

def createnode(ilist, idx):
    nChild = ilist[idx]
    nMeta = ilist[idx+1]
    cidx = idx + 2
    node = Node(nChild, nMeta)
    for i in range(0, nChild):
        child, cidx = createnode(ilist, cidx)
        node.children.append(child)
    for i in range(0, nMeta):
        node.metadata.append(ilist[cidx])
        cidx+=1
    return (node, cidx)

def summeta(node):
    sum = 0
    for i in node.children:
        sum += summeta(i)
    for i in node.metadata:
        sum += i
    return sum

def printnode(node):
    print("node: %d, %d"%(node.cCount, node.mCount))
def calcnodeval(node):
    print("node: %d, %d"%(node.cCount, node.mCount))
    val = 0
    if len(node.children) == 0:
        print("no children")
        for i in node.metadata:
            val += i
        return val
    else:
        for i in node.metadata:
            if i == 0:
                continue
            elif i <= len(node.children):
                
                print("meta: %d"%i)
                childnode = node.children[i-1]
                val += calcnodeval(childnode)
        return val
# part1()
part2()