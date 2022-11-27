from turtle import *

import math
import time

shape('turtle')
speed(0)
pensize(5)

def square(side):
    for i in range(4):
        fd(side)
        rt(90)
        
def rect_prism(short, long):
    square(short)
    lt(45)
    fd(long)
    rt(45)
    fd(short)
    rt(135)
    fd(long)
    bk(long)
    lt(45)
    fd(short)
    rt(45)
    fd(long)
    
    
rect_prism(80,200)

time.sleep(2)
clearscreen()

shape('turtle')
speed(0)
pensize(5)
ht()
def triangle(side):
    for i in range(3):
        fd(side)
        lt(120)
        
def tri_prism(short,long):
    triangle(short)
    lt(60)
    fd(short)
    rt(30)
    fd(long)
    rt(90)
    fd(short)
    rt(90)
    fd(long)
    pu()
    seth(45)
    fd(30)
    pd()
    
    
tri_prism(100,200)

exitonclick()