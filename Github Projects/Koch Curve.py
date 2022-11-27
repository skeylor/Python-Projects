from turtle import *
speed(0)
delay(0)
ht()
pensize(3)
bgcolor('black')
pu()
setx(-200)
sety(250)
pd()
  
colors = ['red','deepskyblue','hotpink','turquoise','magenta','cyan']
def koch(length):
    """Draws a koch curve with the variable length as distance moving fd"""
    if length < 10:
        fd(length)
        pencolor(colors[0])
        return
    new_length = length/3
    pencolor(colors[1])
    koch(new_length)
    pencolor(colors[2])
    lt(60)
    koch(new_length)
    pencolor(colors[3])
    rt(120)
    koch(new_length)
    pencolor(colors[4])
    lt(60)
    koch(new_length)
    pencolor(colors[5])

    


def kochs(size):
    for i in range(3):
        koch(size)
        rt(120)

kochs(500)

exitonclick()