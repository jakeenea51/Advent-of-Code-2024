#!/usr/bin/env python3
# https://adventofcode.com/2024/day/6

from itertools import cycle
from tqdm import tqdm

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()


## PART 1

uniqueSteps = 1
listSteps = []
directions = cycle([lambda x,y: [x,y-1], lambda x,y: [x+1,y], lambda x,y: [x,y+1], lambda x,y: [x-1,y]])
curDir = next(directions)

# function to mark spot as already covered
def mark_spot(l, coord, char):
    strlist = list(l)
    strlist[coord[0]] = char
    return "".join(strlist)

# find starting point
for l in lines:
    if "^" in l:
        sloc = [l.index("^"), lines.index(l)]
        break

# check next loc, then move accordingly
curLoc = sloc
while 0 < curLoc[0] < len(lines[curLoc[1]])-1 and 0 < curLoc[1] < len(lines)-1:
    nextLoc = curDir(curLoc[0],curLoc[1])
    if lines[nextLoc[1]][nextLoc[0]] == "#":
        curDir = next(directions)
    else:
        if lines[nextLoc[1]][nextLoc[0]] != "X":
            uniqueSteps += 1
            listSteps.append(nextLoc)
            lines[nextLoc[1]] = mark_spot(lines[nextLoc[1]], nextLoc, "X")
        curLoc = nextLoc


## PART 2

possibleLoops = 0

# if num steps > area of grid, a loop exists
def isloop(obstacle):
    # reset directions
    directions = cycle([lambda x,y: [x,y-1], lambda x,y: [x+1,y], lambda x,y: [x,y+1], lambda x,y: [x-1,y]])
    curDir = next(directions)
    curLoc = sloc
    steps = 0
    while 0 < curLoc[0] < len(lines[curLoc[1]])-1 and 0 < curLoc[1] < len(lines)-1:
        nextLoc = curDir(curLoc[0],curLoc[1])
        if lines[nextLoc[1]][nextLoc[0]] == "#" or nextLoc == obstacle:
            curDir = next(directions)
        else:
            curLoc = nextLoc
        steps += 1
        if steps > (len(lines[0]) * len(lines)):
            return True
    return False

# try putting obstacles on each coordinate on guard's original path and check if it loops
for i in tqdm(listSteps):
    if isloop(i):
        possibleLoops += 1


print(f"Part 1: {uniqueSteps}")
print(f"Part 2: {possibleLoops}")