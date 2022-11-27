from random import randint

hp = 1000

def rpg (x):
    global hp       # game development instance of when this might be useful.
    if x >= 90:
        print('critical hit!!  You took',x * 3,'damage!!')
        hp = hp - x
        return hp
    else:
        print('You took',x,'damage.')
        hp = hp - x
        return hp
 
rpg(randint(0,100))
print('Your hp is',hp)
 