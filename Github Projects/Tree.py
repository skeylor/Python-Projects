
from turtle import *
shape('turtle')
speed(0)
delay(0)
ht()
seth(90)
colors = ('green','red')
bgcolor('deepskyblue')

def leaf():
    for i in range(2):
        fillcolor(colors[i%2])
        begin_fill()
        circle(10,90)
        lt(90)
        end_fill()

def tree(length, n):
    if n == 0:
        return
    else:
        pencolor('brown')
        fd(length * n)
        lt(20)
        pencolor('green')
        leaf()
        tree(length, n - 1)
        rt(40)
        pencolor('orange')
        leaf()
        tree(length, n - 1)
        lt(20)
        pencolor('brown')
        bk(length * n)
        

tree(3,10)
exitonclick()

        
        
        
        
        