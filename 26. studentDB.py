# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Fri Jan 29 15:05:15 2021
@author: Gyan Krishna

Topic:
"""

roll = []
name = []
marks = []

n = int(input("enter the number of records ::"))
for i in range(n):
    roll.append( int(input("[{}] enter roll ::".format(i))))
    name.append( str(input("[{}] enter name ::".format(i))))
    marks.append(int(input("[{}] enter mark ::".format(i))))
    print("")
max = 0
for i in range(n):
    if(marks[i] > marks[max]):
        max = i

print("roll number = {}, name = {}, marks = {}".format(roll[max], name[max], marks[max]))
