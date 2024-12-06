#!/usr/bin/env python3
# https://adventofcode.com/2024/day/5

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

rules  = [line.split('|') for line in lines if "|" in line]
updates = [line.split(',') for line in lines if "," in line]

## PART 1

answer1 = 0
invalid = []

for u in updates:
    v = []
    for i, num in enumerate(u):
        v += [r for r in rules if (num in r[0] and r[1] in u[:i]) or (num in r[1] and r[0] in u[i:])]
    if len(v) == 0:
        answer1 += int(u[int(len(u)/2)])
    else:
        invalid.append(u)


## PART 2

answer2 = 0

for u in invalid:
    valid = False
    while not valid:
        for i, num in enumerate(u):
            v = [r for r in rules if (num in r[0] and r[1] in u[:i]) or (num in r[1] and r[0] in u[i:])]
            if len(v) > 0:
                temp = u[u.index(v[0][0])]
                u[u.index(v[0][0])] = u[u.index(v[0][1])]
                u[u.index(v[0][1])] = temp
                break
        if len(v) == 0:
            valid = True
    answer2 += int(u[int(len(u)/2)])


print(f"Part 1: {answer1}")
print(f"Part 2: {answer2}")