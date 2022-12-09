
import time

# This first method will print all of the jokes in a row
# The only down side to this method is the inability to exit the joke loop

'''
jokes = ['My wife told me to stop acting like a flamingo...','I had to put my foot down',
         'Why does Waldo wear stripes?','Because he doesn’t want to be spotted.',
         'What do you call a sad cup of coffee?', 'Depresso.']

# The joke and the punchline are separated by commas to allow for the time delay

jokes = [(time.sleep(2), print(i)) for i in jokes]

# Uses a list comprehension to iterate through the list with a print and time delay
'''



myjokes = ['My wife told me to stop acting like a flamingo...','So, I had to put my foot down',
         'Why does Waldo wear stripes?','Because he doesn’t want to be spotted.',
         'What do you call a sad cup of coffee?', 'Depresso.']

# Same list notation as before


time.sleep(1)
i = 0
#joke_response = input('Would you like to hear a joke? ')
#if any(x in joke_response for x in('yes','yeah','y','okay','ok','sure','fine','yup','ye')):
print('Okay, loading joke...')
time.sleep(1)
while i < 6: # while loop that will run until the list indices are out of range.
    print(myjokes[i]) # Grabs the first index of the list as a variable named i.
    print()
    i += 1 # Grabs the second element in the list since the variable has been redefined.
    time.sleep(2)
    print(myjokes[i])
    print()
    time.sleep(1)
    i += 1
    another_joke = input('Would you like to hear another joke? ')
    if i == 6:
        print('Sorry, I am all out of jokes')
        break
    
    elif any (x in another_joke for x in('no','n','negative','nah','negatory')):
        break
    

    
