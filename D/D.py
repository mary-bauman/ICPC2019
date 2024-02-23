
from collections import defaultdict


pulsesTotal = int(input())
hs = set()
vs = set()

for pulse in range(pulsesTotal):
    line = input().split()
    direction = line[0]
    startTime = int(line[1])
    pulseLen = int(line[2])
    wireNum = int(line[3])
    if direction == "h":
        hs.add((startTime, pulseLen, wireNum))
    else:
        vs.add((startTime, pulseLen, wireNum))

count = 0

# check horizontals to see if they match verticals
print(hs)
for horPulse in hs:
    for verPulse in vs:
        print(f"horPulse: {horPulse}")
        print(f"verPulse: {verPulse}")

        #check if they are compatible
        # startTimeDiff = abs(horPulse[0] - verPulse[0])
        # lenDiff = abs(horPulse[1] - verPulse[1])
        # wireDiff = abs(horPulse[2] - verPulse[2])

        #so lets check when this vertical pulse passes through our horizontal pulse
        

print(count)


