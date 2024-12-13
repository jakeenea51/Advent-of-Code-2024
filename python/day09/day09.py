#!/usr/bin/env python3
# https://adventofcode.com/2024/day/9

from tqdm import tqdm

with open("input.txt", "r", encoding="utf8") as f:
    line = f.read().splitlines()
    line = list(line[0])


## PART 1

# expand fileIDs
newFilesystem = []
for i, l in enumerate(line):
    if i > 0:
        fileId = str(int(i/2))
    else:
        fileId = 0
    for d in range (0, int(l)):
        if i % 2 == 0:
            newFilesystem.append(fileId)
        else:
            newFilesystem.append(".")

# trim dots from end of array
def trim():
    while newFilesystem[-1] == ".":
        newFilesystem.pop()

checksum = 0
trim()

# sort new filesystem and calculate checksum
for i, file in enumerate(newFilesystem):
    if "." in newFilesystem:
        if file == ".":
            movingFileIndex = len(newFilesystem)-1
            newFilesystem[i], newFilesystem[movingFileIndex] = newFilesystem[movingFileIndex], newFilesystem[i]
            trim()
        checksum += i * int(newFilesystem[i])
    else:
        break


print(f"Part 1: {checksum}")
# print(f"Part 2: {}")