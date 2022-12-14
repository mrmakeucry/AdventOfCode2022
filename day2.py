# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:18:06 2022

@author: A200014490
"""

# Advent of Code Day 2


# get Input

with open("day2input.txt", 'r') as f:
    _input = f.readlines()
    
    # Part 1


res = 0
my_score = 0

value = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
    }

for line in _input:
    
    enemy_move = line[0] 
    my_move = line[2]

    difference = value[enemy_move] - value[my_move]

    if (difference == 0):
        # Draw 
        my_score += value[my_move] + 3
    elif (difference == 2):
        # Win
        my_score += value[my_move] + 6
    elif (difference == 1):
        # Loss
        my_score += value[my_move]
    
    elif (difference == -1):
        # Win
        my_score += value[my_move] + 6
    elif (difference == -2):
        # Loss
        my_score += value[my_move]


print(my_score)



    
    
        
    
