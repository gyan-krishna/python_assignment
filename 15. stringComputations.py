# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 00:49:38 2021
@author: Gyan Krishna

Topic:
"""

str1 = input("enter string 1 :: ")
str2 = input("enter string 2 :: ")

concat = str1 + str2
print("concatenated string = ",concat)

rev = str1[::-1]
print("reverse string = ",rev)

vowelCnt = 0
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowelCnt += 1

print("no of vowels in  string = ",vowelCnt)

res=""
for i in str1:
    res += str((int)(i)+2)
print("+2 encrypted string :: ",res)

if(rev == str1):
    print("palindrome string")
else:
    print("not palindrome")

wordCnt = 1
for i in str1:
    if(i == ' '):
        wordCnt += 1
print("number of words = ",wordCnt)

