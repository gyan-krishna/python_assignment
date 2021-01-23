# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan 23 22:59:04 2021
@author: Gyan Krishna

Topic:
"""

class Time:
    def __init__(self, hr, mins):
        self.hr = hr
        self.mins = mins


    def addTime(t1, t2):
        hours = t1.hr + t2.hr
        minutes = t1.mins + t2.mins

        hours += int(minutes / 60)
        minutes %= 60

        sumTime = Time(hours, minutes)
        return sumTime

    def subTime(t1, t2):
        hours = t1.hr - t2.hr
        minutes = t1.mins - t2.mins

        sumTime = Time(hours, minutes)
        return sumTime

    def dispTime(self):
        print("the time is {} hours and {} mins".format(self.hr, self.mins))


print("Time 1 ::")
h1 = int(input("enter hours"))
m1 = int(input("enter mins"))

print("Time 2 ::")
h2 = int(input("enter hours"))
m2 = int(input("enter mins"))


t1 = Time(h1,m1)
t2 = Time(h2,m1)

t3 = Time.addTime(t1, t2)
t4 = Time.subTime(t1, t2)

t3.dispTime()
t4.dispTime()