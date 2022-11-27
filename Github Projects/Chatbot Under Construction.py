'''
Sean Keylor
3/25/22
Chatbot
'''

import re, time, random


greetings = ['hi','hello','sup','howdy','aloha','hola','yoohoo'
             ,'aye','salutations','greetings']

pos_responses = ['well','good','fantastic','great','awesome','positive',
                 'happy','ecstatic','jolly']

neg_responses = ['bad','terrible','horrible','sad']

yes_responses = ['yeah','yes','y','sure','ye','yea','affirmative'
                 ,'definitely','okay','ok','k']

def chat_bot():
    msg = get_user_msg()
    if any(x in msg for x in greetings):
        msg = input('Hello.  How are you today?')
        if any(x in msg for x in pos_responses):
            print('I am happy to hear that.')
        elif any(x in msg for x in neg_responses):
            print('I am sorry to hear that.')
            
    elif 'game' in msg or 'trivia' in msg or 'quiz' in msg:
        msg = input('Do you want to play a game?').lower()
        if any(x in msg for x in yes_responses):
            import QuizGameComputers
        


def get_user_msg():
    msg = input('Enter your message here: ').lower()
    if msg == 'quit':
        exit()
    else:
        parsed_msg = re.findall(r"[\w']+|[.,!?;:]", msg)
        return parsed_msg


  
while True:
    chat_bot()
