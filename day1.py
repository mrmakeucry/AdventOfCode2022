# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:56:37 2022

@author: A200014490
"""
# Advent Of Code Day 1 Challenge

# Part 1

working_cal = 0
elfs = []
with open("day1input.txt", 'r') as f:
    _input = f.readlines()
    for curr_cal in _input:
        try:
            working_cal += int(curr_cal)
        except:
            elfs.append(working_cal)
            working_cal = 0
print(max(elfs))


# Part 2

elfs.sort()
res = elfs[-1] + elfs[-2] + elfs[-3]
print(res)