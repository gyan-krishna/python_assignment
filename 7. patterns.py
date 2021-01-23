# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan 23 23:47:00 2021
@author: Gyan Krishna

Topic:
"""
n = 6

#pattern 1
for i in range(n):
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")

print("\n\n")



#pattern 2
curr = []
prev = [1]
for i in range(n):
    print("", end=" ")
print(1)
for i in range(1,n):
    curr = [1]
    for j in range(1,i):
        curr.append(prev[j]+ prev[j-1])
    curr.append(1)
    prev = curr

    for i in range(n-i):
        print("", end=" ")
    for i in curr:
        print(i, end=" ")

    print("")
print("\n\n")


#pattern 3
text = "ABCD"
for i in range(len(text)+1):
    print(text[0:i])


print("\n\n")

#pattern 4
for i in range(n):
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")

for i in range(n,0,-1):
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")

print("\n\n")

#pattern 5:
for i in range(n,0,-1):
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")

for i in range(n):
    for j in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")
