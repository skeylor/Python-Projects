'''
def print_formatted(number):
    w = len(bin(number)[2:]) #bin includes the 0b which [2:] will trim off
    for num in range(1,number+1): 
        print(f"{num:{w}d} {num:{w}o} {num:{w}X} {num:{w}b}")
'''
# The above is the most elegant as it takes the number in the range
# and type casts it into the decimal, octal, hexadecimal(capitalized),and
# binary.  The w here is storing where in the shell the item should be
# displayed.  The above solution is not mine.

def print_formatted(number):
    length = len(bin(number)[2:])
    for num in range(1,number + 1):
        print(f'{num:{length}d}'.rjust(length),end=' ')
        print(f'{num:{length}o}'.rjust(length),end=' ')
        print(f'{num:{length}X}'.rjust(length),end=' ')
        print(f'{num:{length}b}'.rjust(length))
        
print_formatted(15)
