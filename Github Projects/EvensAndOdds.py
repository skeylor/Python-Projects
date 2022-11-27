from random import randint
pos_responses = ['yes','yeah','ye','y','yea','sure','okay','fine']
humanpoints = 0  #declares a global variable
computerpoints = 0  #declares a global variable

        
def evens_and_odds():
    global humanpoints  #converts a local variable inside the function to a global variable.
    global computerpoints
    yournum = int(input("What number are you gonna pick 1-10: "))
    computernum = randint(1,10)  #picks a random number from 1 to 10 (includes 1 and 10)
    #total = yournum+computernum  ??
    print('Computer number = ',computernum) #will print the accumulated score
    print()  #prints an empty line to make it easier to read
    
    if yournum%2 == 0 and computernum%2 == 0:  #if the user correctly guesses an even number
        print("Fine you win but I am getting very angry with you")
        humanpoints += 1
        print('human points =',humanpoints,'computer points =',computerpoints)
        print()  #will print the score of the user and the computer
        
    elif yournum%2 == 1 and computernum%2 == 1: #correct odd number conditional
        print("Fine you win but I am getting very angry with you")
        humanpoints += 1
        print('human points =',humanpoints,'computer points =',computerpoints)
        print()
        
    else:
        print('Sorry, I win!!')
        computerpoints += 1
        print('human points =',humanpoints,'computer points =',computerpoints)
        print()

# this next block of code is alligned with the conditional statements to automatically run regardless
# of the result.  It will ask if the user wants to play again.

    another_match = input('Would you like to play again?')
    print()
    if any(x in another_match for x in pos_responses):
        evens_and_odds()
    else:
        print('okay, bye then')
        
# this next line breaks indentation to allow the user to decide if they would like to play
# without automatically running the function.

response = input('Would you like to play a game of evens and odds?').lower()

if any(x in response for x in pos_responses):
        print('Okay, let\'s begin')
        evens_and_odds()    

# If the user decides they want to play, it will trigger the conditional above which
# calls the main function, even_and_odds()


'''
elif 'evens' in yourinput and total%2 == 1:

    print("Tie! Another one")
    yourinput = input("Well What'll it be? Evens or Odds:")
    yournum = int(input("Also what number are you gonna pick 1-10 :"))
    computernum = randint(1,10)
    #total = yournum+computernum


elif yourinput == "Odds" or yourinput == "odds" and total%2 ==1:
    print("You chose", yournum)
    print("Computer chose", computernum)
    print("Computer Wins!")
    print("HAHA TAKE THE L YOU BAD L+RATIO GET GOOD SCRUB COUNTER RATIO DIDNT ASK LLLL")
    
    
elif yourinput == "Odds" or "odds" and total%2 == 0:
    print("Tie! Another one")
    yourinput = input("Well What'll it be? Evens or Odds:")
    yournum = int(input("Also what number are you gonna pick 1-10 :"))
    computernum = randint(1,10)
    #total = yournum+computernum
'''