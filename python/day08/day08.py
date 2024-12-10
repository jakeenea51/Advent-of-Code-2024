#!/usr/bin/env python3
# https://adventofcode.com/2024/day/8

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()
    lines = list(map(list, lines))


## PART 1

def on_map(a):
    if 0 <= a[0] < len(l) and 0 <= a[1] < len(lines):
        return True
    else:
        return False
    
def add_antinode(al , antinodes):
    for a in al:
        if a not in antinodes and on_map(a):
            antinodes.append(a)
    return antinodes

antennas = {}
antinodes1 = []
antinodes2 = []
for y, l in enumerate(lines):
    for x, d in enumerate(l):
        if d != ".":
            if d not in antennas:
                antennas.update({d: []})
            else:
                for coord in antennas[d]:
                    dx, dy = coord[0]-x, coord[1]-y
                    a1 = [x-dx, y-dy]
                    a2 = [coord[0]+dx, coord[1]+dy]
                    antinodes1 = add_antinode([a1, a2], antinodes1)
                    antinodes2 = add_antinode([a1, a2, [x,y], coord], antinodes2)


## PART 2

                    while on_map(a1):
                        a1 = [a1[0]-dx, a1[1]-dy]
                        antinodes2 = add_antinode([a1], antinodes2)
                    while on_map(a2):
                        a2 = [a2[0]+dx, a2[1]+dy]
                        antinodes2 = add_antinode([a2], antinodes2)
            antennas[d].append([x,y])


print(f"Part 1: {len(antinodes1)}")
print(f"Part 2: {len(antinodes2)}")