# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan 23 23:42:16 2021
@author: Gyan Krishna

Topic:
"""

marks = []

print("enter marks in 5 subs :: ")
for i in range(5):
    marks.append(int(input()))


per = 0
for i in marks:
    per += i

per /= 5

print("total percentage = ", per)

if(per >= 60):
    print("first class")
elif(per >= 45 and per < 60):
     print("second class")
elif(per >= 30 and per < 45):
     print("third class")
else:
    print("fail")