#!/usr/bin/env python3
# https://adventofcode.com/2024/day/1

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()

l1 = []
l2 = []
for line in lines:
    first, second = line.split()
    l1.append(first)
    l2.append(second)

## PART 1

l1_sorted = sorted(l1)
l2_sorted = sorted(l2)

total_distance = 0
for index, num in enumerate(l1_sorted):
    total_distance += abs(int(l2_sorted[index]) - int(l1_sorted[index]))


## PART 2

similarity_score = 0
for i in l1:
    matches = 0
    for j in l2:
        if int(i) == int(j):
            matches += 1
    similarity_score += matches * int(i)



print(f"Part 1: {total_distance}")
print(f"Part 2: {similarity_score}")