#!/usr/bin/env python3
# https://adventofcode.com/2024/day/4

import re

with open("input.txt", "r", encoding="utf8") as f:
    total_input = f.read()
    lines = total_input.splitlines()


## PART 1
answer1 = 0

def valid(a, b, c, d):
    return (a + b + c + d) == "SAMX" or (a + b + c + d) == "XMAS"

# horizontal -
answer1 += len(re.findall("SAMX", total_input))
answer1 += len(re.findall("XMAS", total_input))

for y in range(137):
    for x in range(140):
        # vertical |
        if valid(lines[y][x], lines[y+1][x], lines[y+2][x], lines[y+3][x]):
            answer1 += 1
        if x <= 136:
            # diagonal \
            if valid(lines[y][x], lines[y+1][x+1], lines[y+2][x+2], lines[y+3][x+3]):
                answer1 += 1
            # diagonal /
            if valid(lines[y][x+3], lines[y+1][x+2], lines[y+2][x+1], lines[y+3][x]):
                answer1 += 1


## PART 2
answer2 = 0

def valid_block(block):
    diag = block[0][0] + block[1][1] + block[2][2]
    antidiag = block[2][0] + block[1][1] + block[0][2]
    return (diag == "SAM" or diag == "MAS") and (antidiag == "SAM" or antidiag == "MAS")

for y in range(138):
    for x in range(138):
        if valid_block([line[x:x+3] for line in lines[y:y+3]]):
            answer2 += 1


print(f"Part 1: {answer1}")
print(f"Part 2: {answer2}")