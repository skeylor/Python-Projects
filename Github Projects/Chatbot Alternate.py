'''
Mr. Keylor
Chatbot
3/2/22
'''
#from turtle import*
import re, time, random, TurtleCircles



print('Welcome to Mr. Keylor\'s Chatbot')
print('Type "q" at any time to exit the program')

#name = input('Enter your name here: ')

greetings = ['hi','hello','hola','howdy','sup','wassup','whats up',
             'aloha','salutations']

pos_responses = ['good','great','well','fantastic','excellent',
                 'wonderful','terrific']

neg_responses = ['bad','awful','terrible','downtrodden','sad','sadge']

how_responses = ['I am just a middle-school chatbot.  How do you expect me to know that?',
                 'Did you try to turn it off and then turn it back on again?']

yes_responses = ['yes','y','ye','yea','sure','affirmative','yep','yup','yessir','yesserdoodle']

else_responses = ['I\'m not sure how to answer that...',
                  'I think the answer you are looking for cannot be computed by this program',
                  'I think the answer is 42',
                  'I have no idea']

def chat_bot():
    msg = user_msg()
    if any(x in msg for x in greetings):
        print('Hello,','How are you today?')
        msg = user_msg()
        if any(x in msg for x in pos_responses):
            print('I am happy to hear that')
        elif any(x in msg for x in neg_responses):
            print('I am sorry to hear that')
            time.sleep(.5)
            print('Do you want to hear a joke? Type "y" or "n"')
            response = user_msg()
            if 'y' in response:
                print('How do you keep an idiot in suspense?')
                
    elif 'game' in msg or 'trivia' in msg or 'quiz' in msg:
        msg = input('Do you want to play a game?')
        if any(x in msg for x in yes_responses):
            import QuizGamePhysics
                
    elif 'who' in msg:
        print('My name is HAL...')
        
    
        
    elif 'how' in msg:
        print(random.choice(how_responses))
        
                
    elif 'how' in msg:
        print('I am only a chatbot.  I just work here.')
    
    elif any(x in msg for x in('rock','paper','scissors')):
        print('scissors')
        
    elif 'numbers' in msg or 'number' in msg:
        comp_num = randint(1,100)
        human_num = int(input('Guess a number from 1 through 100'))
        if comp_num == human_num:
            print('You are correct!!  Congratulations')
        elif comp_num > human_num:
            print('Guess a number that is bigger')
            
        else:
            human_num = int(input('Guess again'))
            
        
    elif 'what' in msg:
        print('I am pretty sure the answer is 42.')
        
    else:
        print(random.choice(else_responses))
        #if response in pos_responses:
            #print('I am happy to hear that')
    


def user_msg():
    msg = input('Enter your message here: ').lower()
    print()
    print('bot: typing... ',end=' ')
    time.sleep(.5)
    if msg == 'q':
        quit()  #exit() will do the same thing
    else:
        parsed_msg = re.findall(r"[\w']+|[.,!?;:]", msg)
        return parsed_msg
    
while True:
    chat_bot()
    
    