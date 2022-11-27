def fizz_buzz(x):
    if x % 15 == 0:
        print('fizz buzz')
    elif x % 5 == 0:
        print('fizz')
    elif x % 3 == 0:
        print('buzz')
    else:
        print('x is not an integer')
    
        
fizz_buzz(3)