english = int(input('Enter number of students who subscribed to English newspaper: '))
num_english = set(input('Enter unique numeric values for each student: ').split()) 
french = int(input('Enter number of students who subscribed to English newspaper: '))
num_french = set(input('Enter unique numeric values for each student: ').split())
print(len(num_english.union(num_french)))

'''
The print statement will find all the numbers that each set has in common and
find the length of the unique values to print the number of students that
are subscribed to at least one of these newspapers.
'''