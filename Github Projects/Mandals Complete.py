from turtle import *
from random import randint, randrange, seed
import time, random
speed(0)
shape('turtle')
delay(0)
ht()
screen = Screen()
screen.setup(width = 0.9,height=0.9,startx = 0,starty=0)
bgcolor('black')
saved_pos = (0,0)
saved_h = 0
colormode(255)
colors = ['black','crimson','green']
color_list = ['deepskyblue','salmon','midnightblue','turquoise','lightgreen','indigo','pink','purple']
def magnet():
    global saved_pos, saved_h
    saved_pos = pos()
    saved_h = heading()

def move():
    setpos(saved_pos)
    seth(saved_h)
    
length = 0
turn = 0
segments = 0

def arm_b(segments):
    magnet()
    seed()
    speed(0)
    delay(0)
    for i in range(segments):
        if i % 2 == 0:
            fd(length)
            rt(turn)
            fd(length)
            lt(turn)
        else:
            circle(length,turn2)
            circle(-length,turn2)
            
'''
for j in range(5):
fd(length/5)
lt(turn/5)
'''           
        


def arm_t(segments):
    magnet()
    seed()
    speed(0)
    delay(0)
    for i in range(segments):
        if i % 2 == 0:
            fd(length)
            lt(turn)
            fd(length)
            rt(turn)
        else:
            circle(-length,turn2)
            circle(length,turn2)
    


def mandala():
    global length, turn, pc, turn2
    speed(0)
    shape('turtle')
    delay(0)
    ht()
    bgcolor(random.choice(colors))
    screen = Screen()
    screen.colormode(255)
    saved_pos = (0,0)
    saved_h = 0
    length = randint(10,80)
    turn = randint(5,120)
    turn2 = randint(40,181)
    segments = randint(2,8)
    width(randint(2,7))
    sides = randrange(6,10)
    pencolor(randrange(0, 255),
            randrange(0, 255),
            randrange(0, 255))
    for i in range(sides):
        arm_b(segments)
        pu()
        move()
        pd()
        arm_t(segments)
        pu()
        move()
        pd()
        rt(360/sides)

def mandalas():
    for i in range(6):
        color(random.choice(color_list))
        begin_fill()
        mandala()
        color(random.choice(color_list))
        end_fill()
    mandala()
    pu()
    setpos(-700,400)
    pd()
    pencolor('white')
    seth(90)
    write('Sean Keylor')
    pu()
    bk(50)
    pd()
    write('Mandala, 10/16/22')

def mandala_animate():
    mandalas()
    #answer = input('Would you like to save this picture?').lower()
    #if answer == 'yes' or 'y' or 'yea' or 'yeah' or 'sure':
        #cv = getcanvas()
        #cv.postscript(file = "mandala.ps")
    time.sleep(1)
    clearscreen()
    mandala_animate()
    
            
mandala_animate()


exitonclick()
