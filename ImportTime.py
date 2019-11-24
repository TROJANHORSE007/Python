# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:10:17 2019

@author: Shubham
"""

import time
def square(n):
    print("this is the function use to find squre")
    for i in n:
        print("squre of {0} is". format(i), i*i)
        time.sleep(0.5)
        
def cube(n):
    print("this is the function use to find cube")
    for i in n:
        print("cube of {0} is". format(i), i*i*i)
        time.sleep(0.5)

t = time.time()        
a = [1,2,3,4,5,6]
square(a)
cube(a)
print("time taken by system is " , time.time()-t )