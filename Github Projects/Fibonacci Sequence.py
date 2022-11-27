def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
    
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
    # Otherwise it will run the fib sequence to find the sum of the two previous numbers.
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 

#print(Fibonacci(10))

# The following fibonacci sequence will put all the numbers in a list to see that
# the sequence is working as intended.

def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

print([fibonacci_of(n) for n in range(10)])