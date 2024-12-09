#!/usr/bin/env python3
# https://adventofcode.com/2024/day/7

from itertools import product
from tqdm import tqdm

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()
    lines = map(lambda x: x.split(": "), lines)


## PART 1

calibrationResult1 = 0

calibrationResult2 = 0

for l in tqdm(lines):
    matched = False
    curTotal, curNums = int(l[0]), list(map(int, l[1].split(" ")))
    combos = list(product(["+", "*"], repeat=len(curNums)-1))
    for c in combos:
        testTotal = curNums[0]
        for i, op in enumerate(c):
            testTotal = eval(str(testTotal) + op + str(curNums[i+1]))
            if testTotal > curTotal:
                break
        if testTotal == curTotal:
            calibrationResult1 += curTotal
            matched = True
            break


## PART 2

    if not matched:
        combos = list(product(["+", "*", "||"], repeat=len(curNums)-1))
        for c in combos:
            testTotal = curNums[0]
            for i, op in enumerate(c):
                if op == "||":
                    testTotal = int(str(testTotal) + str(curNums[i+1]))
                else:
                    testTotal = eval(str(testTotal) + op + str(curNums[i+1]))
                if testTotal > curTotal:
                    break
            if testTotal == curTotal:
                calibrationResult2 += curTotal
                break


calibrationResult2 += calibrationResult1


print(f"Part 1: {calibrationResult1}")
print(f"Part 2: {calibrationResult2}")