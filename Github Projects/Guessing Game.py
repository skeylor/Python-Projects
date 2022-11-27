from random import randint

def guessing_game():
    rando = randint(1,100)
    print("I'm thinking of a number between 1 and 100")
    guess = int(input('Take a guess: '))
    num_of_guess = 1
    while guess:
        if rando == guess:
            print('Wow, lucky guess.')
            print('It took you a number of',num_of_guess,'trys to get the right answer')
            break
        elif guess > rando:
            print ('Try a smaller number')
        elif guess < rando:
            print ('Try a bigger number')
        guess = int(input('Take a guess'))
        num_of_guess += 1
        
guessing_game()
                    

        
    
        
    