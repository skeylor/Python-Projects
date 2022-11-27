
'''
def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return leap
        

'''

'''
year = int(input('Enter your number here: '))
print(is_leap(year))
'''
'''
n = 5
for i in range(1,n):
    print(i,end='')
'''
'''
n = 15
    
def print_formatted(number):
    for i in range(1,number + 1):
        print(f'{i} {oct(i)} {hex(i)} {bin(i)}')
        
print_formatted(n)
'''
'''
n = int(input('Input number of students: '))
student_marks = {}
for _ in range(n):
    name, *line = input('input name of students: ').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('Student name to check average: ')
'''
'''
def swap_case(s):
    letters = list(s)
    changed_case = []
    for letter in letters:
        if letter == letter.upper():
            letter = letter.lower()
            changed_case.append(letter)
        elif letter == letter.lower():
            letter = letter.upper()
            changed_case.append(letter)
    changed_case = ''.join(changed_case)
    print(changed_case)
 

swap_case('HeLLo')
'''
'''
scores = [7,3,9,8,4,5,3,9,7,8]

#scores.sort()
scores = set(scores)
scores = list(scores)
scores.remove(max(scores))
print(max(scores))
'''

'''
for score in range(len(scores)):
    if score == max(score):
        scores.remove(max(scores))
        print(scores)
    
'''
'''
c = 'H'
thickness = 5

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))


#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    


#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    


#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    


def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string

print(mutate_string('hello',4,'p'))


a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))


def merge_the_tools(string, k):
    store = []
    for letter in string:
        for i in range(k):
            store.append(letter)
    print(store)
        
merge_the_tools('AABCAAADA',3)
            
            


n = int(input())
t = ()
for i in range(1,n+1):
    t = t + (i,)
    
print(hash(t))


import textwrap
string = "This is a very very very very very long string."
print (textwrap.fill(string,8))


name = 'sean    keylor'
name = ' '.join([f"{i[:1].upper()}{i[1:].lower()}" for i in name.split(' ')])
print(name)


# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))



s = 'BANANA'

vowels = 'AEIOU'
consonants = 'bcdfghjklmnpqrstvwxyz'.upper()
for letter in s:
    if letter in vowels:
        set_vowels = set_vowels + (letter,)
    else:
        set_cons = set_cons + (letter,)
           

print(set_vowels)
print(set_cons)


# Getting square of from 1 to 10
squares = [number**2 for number in range(1, 21)]
 
# Display square of even numbers
print(squares)

# Reverse print

string = 'banana'

print(string[::-1])

# Reverse each string in tuple
slist = [string[::-1] for string in ('coco', 'for', 'cocopuffs')]
 
# Display list
print(slist)



# All possible permutations with list comprehensions

x = 1
y = 1
z = 2
n = 3

# Print all possible permutations that are not equal (!=) to n

s = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# The last part of a list comprehension has an optional conditional
print(s)


if __name__ == '__main__':
    records = []
    #off by one error
    for n in range(int(input())):
        name = input()
        score = float(input())
        #name will always be in row 0
        records[0][n] = name
        #score will always be in column 1
        records[n][1] = score
    print(records)       
    # sort list of list
    # sort by second index
    records.sort(key = lambda records: records[1])
    records.pop(0)
    second_lowest = []
    if records[0][1] == records[1][1]:
        second_lowest.append(records[0][0])
        second_lowest.append([records[1][0]])
        second_lowest.sort(key = lambda second_lowest: records[0])
        print(second_lowest[0])
        print(second_lowest[1][0])
    else:
        print(records[0][0])
        
'''

# import the modules
import tkinter
import random

# list of possible colour.
colours = ['Red','Blue','Green','Pink','Black',
		'Yellow','Orange','White','Purple','Brown']
score = 0

# the game time left, initially 30 seconds.
timeleft = 30

# function that will start the game.
def startGame(event):
	
	if timeleft == 30:
		
		# start the countdown timer.
		countdown()
		
	# run the function to
	# choose the next colour.
	nextColour()

# Function to choose and
# display the next colour.
def nextColour():

	# use the globally declared 'score'
	# and 'play' variables above.
	global score
	global timeleft

	# if a game is currently in play
	if timeleft > 0:

		# make the text entry box active.
		e.focus_set()

		# if the colour typed is equal
		# to the colour of the text
		if e.get().lower() == colours[1].lower():
			
			score += 1

		# clear the text entry box.
		e.delete(0, tkinter.END)
		
		random.shuffle(colours)
		
		# change the colour to type, by changing the
		# text _and_ the colour to a random colour value
		label.config(fg = str(colours[1]), text = str(colours[0]))
		
		# update the score.
		scoreLabel.config(text = "Score: " + str(score))


# Countdown timer function
def countdown():

	global timeleft

	# if a game is in play
	if timeleft > 0:

		# decrement the timer.
		timeleft -= 1
		
		# update the time left label
		timeLabel.config(text = "Time left: "
							+ str(timeleft))
								
		# run the function again after 1 second.
		timeLabel.after(1000, countdown)


# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("COLORGAME")

# set the size
root.geometry("375x200")

# add an instructions label
instructions = tkinter.Label(root, text = "Type in the colour "
						"of the words, and not the word text!",
									font = ('Helvetica', 12))
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
									font = ('Helvetica', 12))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " +
			str(timeleft), font = ('Helvetica', 12))
				
timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()

        


