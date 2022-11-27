
import math

"""
def plug(): # very limited and basic program that only solves for integers.
    for i in range(1,10):
        if 2 * i + 5 == 13:
            print('x is',i)
        else:
            i += 1
plug()
"""





"""
# will solve for x in an algebraic expression

def algebra():
    x = 1
    while x < 5:
        if 2 * x + 5 == 14: #2x + 5 = 14
            print('x =',x)
        else:
            print('x amount =',x)
            print('Algebraic expression:',2 * x + 5)
        x += .1
        
algebra()
"""






"""
# Solves first-degree equations
def equation(a,b,c,d): 
    # Solves equations of the form ax + b = d or ax + b = cx + d
    # or ax + b = cx + d(in this case c is a place holder for 0.)
    print((d-b)/(a-c)) # prints the answer
    return (d-b)/(a-c) # stores the value of the equation as a fruitful function
#ex. 3x - 5 = 22 or 12x + 18 = -34x + 67

equation(12,18,-34,67) # solves for x
x = equation(12,18,-34,67) # stores the value of x as a variable

print(12*x+18) # checking that my answers match
print(-34*x +67)
"""






"""
def quad(a,b,c):
    # Solves quadratic equations
    # Ex. x ** 2 + 3x - 10 = 0
    # Always contains an x variable squared
    # The variable equation = ax**2 + bx + c = 0
    # a in this case is = to 1
    x_add = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2*a)
    x_minus = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2*a)
    return(x_add,x_minus)

x = quad(2,7,-15)
print(x)
"""
# Solves qubic equations

# 6x + 31x**3 + 3x - 10 = 0
def cubic(a,b,c,d):
    x = -50
    while x < 50:
        if a * x**3 + b * x**2 + c * x + d == 0:
            print('x =',x)
            break
        x += 1
        
cubic(2,3,-11,-6)