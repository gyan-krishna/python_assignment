# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Fri Jan 29 14:50:50 2021
@author: Gyan Krishna

Topic: operations on set
"""


n = int(input("enter the number of elements ::"))

seta = set()
setb = set()

for i in range(n):
    seta.add(int(input("enter member of set A ::")))

for i in range(n):
    setb.add(int(input("enter member of set B ::")))

union = seta.union(setb)
intersection = seta.intersection(setb)
differrence = seta.difference(setb)

print("Set A        ::",seta)
print("Set B        ::",setb)
print("Union        ::",union)
print("Intersection ::",intersection)
print("differrence  ::",differrence)