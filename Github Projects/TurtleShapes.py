from turtle import *
import time

colors = ['orange','hotpink','deepskyblue','white','turquoise','red','purple']
speed(0)
delay(0)
ht()
bgcolor('black')

def settings():
    time.sleep(1)
    clearscreen()
    speed(0)
    delay(0)
    ht()
    bgcolor('black')
    time.sleep(1)
    
def square(length):
    for i in range(4):
        fd(length)
        rt(90)

def multi_square(length):
    for i in range(60):
        pencolor(colors[i%7])
        square(length)
        rt(5)
        length += 5
        
def star(length):
    for i in range(5):
        fd(length)
        rt(144)

def star_spiral(length):
    for i in range(60):
        pencolor(colors[i%7])
        star(length)
        rt(5)
        length += 5
        

def sun(length, turn):
    for i in range(42):
        pencolor(colors[i%7])
        circle(length)
        rt(turn)
        length += 5
        turn -= 2


def spirograph(size):
    for i in range(30):
        pencolor(colors[i%7])
        circle(size)
        rt(12)
        

def circles(x):
    for i in range(200):
        pencolor(colors[i%7])
        circle(i)
        rt(5)

   

def all_pictures():
    settings()
    circles(10)
    settings()
    multi_square(5)
    settings()
    star_spiral(5)
    settings()
    sun(20,42)
    settings()
    spirograph(200)

all_pictures()
exitonclick()