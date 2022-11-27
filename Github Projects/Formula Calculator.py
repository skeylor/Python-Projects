import math

def distance(x1,y1,x2,y2): #Coordinates in the order they appear
    d = ((x2-x1)**2 + (y2 - y1) ** 2) #Formula for distance
    print('The square root of',d,'is your answer')       
    #This answer is incomplete as the computer will simplify
    #the answer as a decimal.  It is up to the user to simplify the radical.
    
distance(1,7,5,-1)

# Coordinates (1,7) and (5,-1)

def midpoint(x1,y1,x2,y2):
    mpx = ((x1 + x2)/2)
    mpy = ((y1 + y2)/2)
    x = mpx
    y = mpy
    print('The coordinates = (',x,',',y,')')

midpoint(1,7,5,-1)
    
'''   
def function():
    numbers = int(input('How many numbers do you want to check? '))
    for i in range(numbers):
        num = int(input('Type your first number: '))
        y = 2 * num + 3
        print('y =',y,'when function of x =',num,'\n')
        
# f(x) = 2(x) + 3    
    
function()
'''
# solve for 5, -3, 8, 13

def quad(a,b,c):
    solution = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    print('Solution to quadratic equation =',solution)
    
quad(6,-17,12)

'''
def brutus():
    x = -10
    while x < 10:
        x = round(x,3)
        if 12 * x + 2.54 == 78.74:
            print('The answer =',x)
        else:
            pass#print(x)
        x+=.01

brutus()
'''

def radius(circum):
    rad = circum/(math.pi * 2)
    print('radius =',rad)
    return rad

def circle_area(radius):
    area = math.pi * radius ** 2
    print('area =',area)
    return area

circle_area(radius(60))

