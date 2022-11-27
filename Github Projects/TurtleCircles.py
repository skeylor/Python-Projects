from turtle import*
shape('turtle')
colors = ['pink','purple','deepskyblue','red','cyan','hotpink','turquoise']
bgcolor('black')
speed(0)
delay(0)
pencolor('white')
ht()
write('hello, world',False,'center',('Arial',29,'normal'))

def shrink(x):
    while x > 1:
        circle(x)
        x -= 10
        
def grow(y):
    while y < 200:
        circle(y)
        y += 10

def shrink_grow(x,y):
    shrink(x)
    rt(180)
    grow(y)
    
shrink_grow(200, 10)

for i in range(200):
    pencolor(colors[i%7])
    circle(i)
    rt(90)
    circle(i)

exitonclick()
