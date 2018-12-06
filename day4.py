from collections import namedtuple
Log = namedtuple("Time", ["month", "day", "hour", "minutes", "activity"])

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
                    guardsmap[guardid] = 0
            month = int(timestamp.split("-")[1])
            day = int(timestamp.split("-")[2].split(" ")[0])
            time = timestamp.split("-")[2].split(" ")[1]
            hour = int(time.split(":")[0])
            if hour == 0:
                hour = 24
            minutes = int(time.split(":")[1])
            log = Log(month, day, hour, minutes, activity)
            logs.append(log)
        logs = sorted(logs, key = lambda x: (x.month, x.day, x.hour, x.minutes))

        currG = None
        for line in logs:
            if "Guard" in line.activity:
                currG = activity.split("#")[1].split(" ")[0]
                continue


        # for log in logs:
        #     f2.write("%d"%log.month)
        

part1()