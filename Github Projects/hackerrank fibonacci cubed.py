cube = lambda x: x**3
n = 5
def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

arr = [fibonacci(n) for n in range(n)]
print(arr)
final = []
for num in arr:
    final.append(cube(num))
    
print(final)
    
    
