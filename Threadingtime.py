# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:22:48 2019

@author: Shubham
"""


import threading as ti 
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
t1 = ti.Thread(target = square , args = (a,))
t2 = ti.Thread(target = cube , args = (a,))
t1.start()
t2.start()
t1.join()
t2.join()

print("time taken by system is " , time.time()-t )