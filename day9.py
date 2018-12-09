class Player:
    def __init__(self, id):
        self.id = id
        self.score = 0

class Marble:
    def __init__(self, id):
        self.id = id
        self.clockwise = self
        self.cclockwise = self

    def Remove(self):
        self.clockwise.cclockwise = self.cclockwise
        self.cclockwise.clockwise = self.clockwise
    
    def AddClockwise(self, marble):
        self.clockwise.cclockwise = marble
        marble.clockwise = self.clockwise
        self.clockwise = marble
        marble.cclockwise = self

def part1():
    currM = Marble(0)
    marble0 = currM
    players = []
    for i in range(0,418):
        players.append(Player(i))
    
    curPIdx = 0
    for i in range(1,7134000):

        if curPIdx >= len(players):
            curPIdx = 0
        curP = players[curPIdx]
        if i %23 == 0:
            curP.score+=i
            marbleToRemove = currM.cclockwise.cclockwise.cclockwise.cclockwise.cclockwise.cclockwise.cclockwise
            currM = marbleToRemove.clockwise
            curP.score += marbleToRemove.id
            marbleToRemove.Remove()
            curPIdx+=1
        else:
            cM = currM.clockwise
            newM = Marble(i)
            cM.AddClockwise(newM)
            currM = newM
            curPIdx += 1
    max = 0

    for i in players:
        print("player %d: score %d"%(i.id, i.score))
        if i.score > max:
            max = i.score
    print(max)

part1()