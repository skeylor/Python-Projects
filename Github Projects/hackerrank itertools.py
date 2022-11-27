from itertools import product

'''
itertools.product()

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

'''
a = map(int, input().split())
b = map(int, input().split())
a_b = list(product(a,b))
for i in range(len(a_b)):
    print(a_b[i], end=' ')
    
    
'''
Python's map() is a built-in function that allows you to process
and transform all the items in an iterable without using an explicit
for loop, a technique commonly known as mapping. map() is useful when
you need to apply a transformation function to each item in
an iterable and transform them into a new iterable.
'''
