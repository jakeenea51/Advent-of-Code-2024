#!/usr/bin/env python3
# https://adventofcode.com/2024/day/2

with open("input.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()


## PART 1

def part1():
    num_safe_reports = 0
    for line in lines:
        safe = True
        temp_list = list(map(int, line.split()))
        if temp_list == sorted(temp_list) or temp_list == sorted(temp_list, reverse=True):
            for index, num in enumerate(temp_list):
                if index > 0:
                    if abs(num - temp_list[index-1]) > 3 or abs(num - temp_list[index-1]) < 1:
                        safe = False
                        break
        else:
            safe = False
        if safe == True:
            num_safe_reports += 1
    return num_safe_reports
                

## PART 2
def part2():
    num_safe_reports = 0
    second_chances = []

    # for line in lines:
    #     safe = True
    #     increasing = True
    #     temp_list = list(map(int, line.split()))
    #     for index, num in enumerate(temp_list):
    #         if index > 0:
    #             if index == 1:
    #                 if num - temp_list[index-1] < 0:
    #                     increasing = False
    #                 elif num - temp_list[index-1] == 0:
    #                     safe = False
    #             else:
    #                 if (increasing == True and num - temp_list[index-1] < 0) or (increasing == False and num - temp_list[index-1] > 0):
    #                     safe = False
    #             if abs(num - temp_list[index-1]) > 3 or abs(num - temp_list[index-1]) < 1:
    #                 safe = False
    #         if safe == False:
    #             #print(temp_list)
    #             if index < len(temp_list)-1:
    #                 if (increasing == True and num - temp_list[index+1] < 0):
    #                     temp_list.pop(index-1)
    #                 elif (increasing == False and num - temp_list[index+1] > 0):
    #                     temp_list.pop(index-1)
    #             else:
    #                 temp_list.pop(index)
    #             #print(temp_list)
    #             second_chances.append(temp_list)
    #             break
    #     if safe == True:
    #         #print(temp_list)
    #         num_safe_reports += 1

    def valid(line):
        safe = True
        if isinstance(line, str):
            temp_list = list(map(int, line.split()))
        else:
            temp_list = line
        if temp_list == sorted(temp_list) or temp_list == sorted(temp_list, reverse=True):
            for index, num in enumerate(temp_list):
                if index > 0:
                    if abs(num - temp_list[index-1]) > 3 or abs(num - temp_list[index-1]) < 1:
                        safe = False
                        break
        else:
            safe = False
        return safe

    for line in lines:
        if valid(line) == False:
            second_chances.append(line)

    for line in second_chances:
        reset_list = list(map(int, line.split()))
        for index in range(len(reset_list)):
            temp_list = reset_list.copy()
            temp_list.pop(index)
            if valid(temp_list):
                num_safe_reports += 1
                break


    return num_safe_reports   



print(f"Part 1: {part1()}")
print(f"Part 2: {part1() + part2()}")