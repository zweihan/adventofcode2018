import heapq
import time
class Node:
    def __init__(self, name):
        self.name = name
        self.pre = []
        self.des = []
        self.marked = False


def readinput():
    inputs = []
    f = open("day7_input.txt",'r')
    for line in f:
        before = line.split(" ")[1]
        after = line.split(" ")[7]
        input = (before,after)
        inputs.append(input)
    return inputs

def part1():
    inputs = readinput()
    nodesdict = dict()
    for line in inputs:
        prenode = None
        desnode = None
        if line[0] not in nodesdict.keys():
            prenode = Node(line[0])
        else:
            prenode = nodesdict[line[0]]
        prenode.des.append(line[1])
        nodesdict[prenode.name] = prenode
        if line[1] not in nodesdict.keys():
            desnode = Node(line[1])
        else:
            desnode = nodesdict[line[1]]
        desnode.pre.append(line[0])
        nodesdict[desnode.name] = desnode
    queue = []
    for node in nodesdict.keys():
        if len(nodesdict[node].pre) == 0:
            queue.append(nodesdict[node].name)
    queue.sort()
    fulfilledqueue = queue
    unfulfilledqueue = []
    order = ""
    while len(fulfilledqueue) > 0:
        cnid = heapq.heappop(fulfilledqueue)
        cnode = nodesdict[cnid]
        order += cnid
        desc = cnode.des
        for d in desc:
            if d not in unfulfilledqueue:
                unfulfilledqueue.append(d)
        for n in unfulfilledqueue:
            node = nodesdict[n]
            fulfilled = True
            for s in node.pre:
                if s not in order:
                    fulfilled = False
            if fulfilled:
                unfulfilledqueue.remove(n)
                heapq.heappush(fulfilledqueue,n)

    print(order)
    # for node in nodesdict.keys():
    #     print("%s"%nodesdict[node].name)
    # print(inputs)

part1()