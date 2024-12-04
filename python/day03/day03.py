#!/usr/bin/env python3
# https://adventofcode.com/2024/day/3

import re

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read()


## PART 1

matches = []
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches.extend(re.findall(pattern, lines))
total1 = 0
for pair in matches:
    total1 += int(pair[0]) * int(pair[1])


## PART 2

matches = []
pattern = r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)"
matches.extend(re.findall(pattern, lines))
total2 = 0
enabled = True
for match in matches:
    print(match)
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        if enabled:
            pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
            pair = re.findall(pattern, match)
            total2 += int(pair[0][0]) * int(pair[0][1])


print(f"Part 1: {total1}")
print(f"Part 2: {total2}")