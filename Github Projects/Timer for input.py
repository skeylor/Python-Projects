from threading import Timer
import time

def game_over():
    print('This is the end my friend.')
    print('Game over....')
    input('If you want to play again, press enter')


def boss_fight():
    print('After getting the answer right, the troll dissapears into a curl of smoke and ash.')
    print('You continue down the dank and dimly lit hallway until you see a door that reads:')
    print('No Noobs Beyond this Point.')
    print('You steady your sword and prepare to lunge at whatever awaits behind the door.')
    
timeout = 10
def quicktime(seconds):
    t = Timer(timeout, function=game_over)
    t.start()
    prompt = "You have %d seconds to answer the riddle:  \n \nAlive without breath, \nAs cold as death; \nNever thirsty, ever drinking,\nAll in mail never clinking.?...\n" % timeout
    answer = input(prompt)
    if answer == 'fish':
        print('Well done...Time for a real challenge.')
        time.sleep(1)
        boss_fight()
    else:
        print('try again')
        quicktime(timeout)
    t.cancel()

quicktime(timeout)
#game_over()


