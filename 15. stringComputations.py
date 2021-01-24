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
    if(i.isalpha()):
        res += chr((ord)(i)+2)
    else:
        res+= i
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

wrd = ""
initials1 = ""
str3 = str1 + " "
for i in str3:
    if(i == " "):
        initials1 += wrd[0] + "."
        wrd = ""
    else:
        wrd += i

print(initials1)

wrd = ""
initials2 = ""
for i in str1:
    if(i == " "):
        initials2 += wrd[0] + "."
        wrd = ""
    else:
        wrd += i

initials2 += wrd
print(initials2)

consless = ""
for i in range(len(str1)-1):
    if(str1[i] != str1[i+1]):
        consless += str1[i]
consless += str1[len(str1)-1]
print(consless)

