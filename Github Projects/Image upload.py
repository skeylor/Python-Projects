from tkinter import *
import time


window = Tk()
window.title('Add Image')
window = Canvas(window,width = 2000, height = 1000)
window.pack()
image = PhotoImage(file = 'C:\\Users\\seank\\Desktop\\hi.png')

def decision():
    time.sleep(2)
    print('You are unsure what to do next.')
    print('Should you')
    print('1. Run away and find help')
    print('2. Take the fight to the enemy')
    input()

def clue():
    print('On a crumpled note left on the window sill read the following message...')
    time.sleep(2)
    window.create_image(0,0,anchor = NW, image = image)
    
   
    
    

clue()
window.mainloop()
decision()





