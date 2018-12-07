from collections import namedtuple
Log = namedtuple("Time", ["month", "day", "hour", "minutes", "activity"])
class Guard:
    def __init__(self,id):
        self.id = id
        self.minutes = 0
        self.logsapp = []
def part1():
    with open("day4_input.txt", 'r') as f:
        logs = []
        guardsmap = dict()
        for line in f:
            timestamp = line.split("]")[0]
            activity = line.split("]")[1].strip()
            if "Guard" in activity:
                guardid = activity.split("#")[1].split(" ")[0]
                if guardid not in guardsmap.keys():
                    guardsmap[guardid] = Guard(guardid)
            month = int(timestamp.split("-")[1])
            day = int(timestamp.split("-")[2].split(" ")[0])
            time = timestamp.split("-")[2].split(" ")[1]
            hour = int(time.split(":")[0])
            minutes = int(time.split(":")[1])
            log = Log(month, day, hour, minutes, activity)
            logs.append(log)
        logs = sorted(logs, key = lambda x: (x.month, x.day, x.hour, x.minutes))
        with open("day4_input_sorted.txt", 'w') as w:
            for line in logs:
                w.write("%02d-%02d %02d:%02d - %s\n"%(line.month, line.day, line.hour, line.minutes, line.activity))
        currG = None
        prevLog = None
        for line in logs:
            if "Guard" in line.activity:
                currG = guardsmap[line.activity.split("#")[1].split(" ")[0]]
                prevLog = line
                currG.logsapp.append(line)
                continue
            else:
                currG.logsapp.append(line)
                if "wakes" in line.activity:
                    # print("#%s: %d"%(currG.id,currG.minutes))
                    # print(prevLog)
                    # print(line)
                    duration = getDuration(prevLog, line)
                    currG.minutes += duration
                prevLog = line
        maxguard = None
        for key in guardsmap.keys():
            g = guardsmap[key]
            if maxguard == None or g.minutes > maxguard.minutes:
                maxguard = g
        w = open("day4_input_g.txt",'w')
        for line in maxguard.logsapp:
            w.write("%02d-%02d %02d:%02d - %s\n"%(line.month, line.day, line.hour, line.minutes, line.activity))
        w.close()
        idx,maxv = maxminute(maxguard)
        print(idx * int(maxguard.id))


def part2():
     with open("day4_input.txt", 'r') as f:
        logs = []
        guardsmap = dict()        
        for line in f:
            timestamp = line.split("]")[0]
            activity = line.split("]")[1].strip()
            if "Guard" in activity:
                guardid = activity.split("#")[1].split(" ")[0]
                if guardid not in guardsmap.keys():
                    guardsmap[guardid] = Guard(guardid)
            month = int(timestamp.split("-")[1])
            day = int(timestamp.split("-")[2].split(" ")[0])
            time = timestamp.split("-")[2].split(" ")[1]
            hour = int(time.split(":")[0])
            minutes = int(time.split(":")[1])
            log = Log(month, day, hour, minutes, activity)
            logs.append(log)
        logs = sorted(logs, key = lambda x: (x.month, x.day, x.hour, x.minutes))
        for line in logs:
            if "Guard" in line.activity:
                currG = guardsmap[line.activity.split("#")[1].split(" ")[0]]
                prevLog = line
                currG.logsapp.append(line)
                continue
            else:
                currG.logsapp.append(line)
                if "wakes" in line.activity:
                    # print("#%s: %d"%(currG.id,currG.minutes))
                    # print(prevLog)
                    # print(line)
                    duration = getDuration(prevLog, line)
                    currG.minutes += duration
                prevLog = line
        maxidx = -1
        maxv = -1
        maxguard = None
        for guard in guardsmap.keys():
            idx, v = maxminute(guardsmap[guard])
            if v > maxv:
                maxidx = idx
                maxv = v
                maxguard = guard
        print(maxidx * int(guardsmap[maxguard].id))


def maxminute(guard):
    minuteLog = []
    for i in range(0,61):
        minuteLog.append(0)
    prevLog = None
    maxIdx = -1
    maxv = -1
    for line in guard.logsapp:
        if "Guard" in line.activity:
            prevLog = line
            continue
        else:
            
            if "wakes" in line.activity:
                sleepspan = getSpan(prevLog, line)
                
                if sleepspan[1] == -1:
                    continue
                for i in range(sleepspan[0], sleepspan[1]+1):
                    minuteLog[i] +=1
                    if minuteLog[i] > maxv:
                        maxv = minuteLog[i]
                        maxIdx = i
            prevLog = line
    return (maxIdx, maxv)


def getDuration(line1,line2):
    line1min = line1.minutes
    if line1.hour == 24:
        line1min += 60
    line2min = line2.minutes
    if line2.hour == 24:
        line2min += 60
    duration = line2min - line1min
  # subtract out minutes within hour 23
    if line1.hour == 23:
        duration -= 60 - line1min.minutes

    return duration



def getSpan(line1, line2):
    firstdigit = -1
    seconddigit = -1
    if line1.hour == 23:
        firstdigit = 0
    else:
        firstdigit = line1.minutes
    if line2.hour == 23:
        seconddigit = -1
    else:
        seconddigit = line2.minutes-1

    return (firstdigit,seconddigit)
        # for log in logs:
        #     f2.write("%d"%log.month)
        

part1()
part2()