import time
import os
import sys
import enemy_class

camels = 42
print('%d' % camels)

border = '-'*80
name = ''
gen = ''
character = ''
pro = ''

def intro():
    while True:
        print('Welcome to Elysium: the magical world of wizards, warriors, and warlocks!!')
        print(border)
        print('Type 1 if you want to start your adventure')
        print('Type 2 if you want to load your last adventure')
        print('Type 3 if you want to exit the game')
        print(border)
        ans = input("What'll it be: ")
        if ans == '1':
            character_class()
            continue
        elif ans == '2':
            pass
        elif ans == '3':
            break
        else:
            print('Enter a valid input')

def setup():
    global name, gen
    print('Welcome, brave adventurer.')
    name = input('What should I call ya: ')
    gen = input('Are you a boy or a girl?')
    
    
class Character():
    
    def __init__(self,name,gen,char):
        self.name = name
        self.gen = gen
        self.char = char
        
# sp: subjective pronoun
# op: objective pronoun
# pp: possessive pronoun

        if self.gen == 'm':
            self.sp = 'he'
            self.op = 'him'
            self.pp = 'his'
            
        elif self.gen == 'f':
            self.sp = 'she'
            self.op = 'her'
            self.pp = 'hers'
            
        if self.char == 'warrior':
            self.str = 100
            self.int = 30
            self.mana = 10
            self.agi = 20
            self.hp = 90
        elif self.char == 'mage':
            self.str = 30
            self.int = 100
            self.mana = 90
            self.agi = 10
            self.hp = 30
        elif self.char == 'ranger':
            self.str = 50
            self.int = 50
            self.mana = 45
            self.agi = 95
            self.hp = 45



def character_description():
    print('The warrior is strong and fierce but lacks agility and mana.')
    print('The mage is wise and powerful but it susceptible to physical attacks.')
    print('The ranger is agile and quick but lacks strength and magic.')
    response = input('Got all that?  Type yes to pick your character.').lower()
    if response == 'yes':
        character_class()
    else:
        character_description()
        
def character_class():
    global char
    print('Type 1 to play as the warrior.')
    print(border)
    print('Type 2 to play as the mage.')
    print(border)
    print('Type 3 to play as the ranger.')
    print(border)
    print('Type 4 to learn more about the strengths and weaknesses of the character classes.')
    response = input("What'll it be then: ")
    if response == '1':
        char = 'warrior'
        Character(name,gen,char)
        adventure_start()
    elif response == '2':
        char = 'mage'
        Character(name,gen,char)
        adventure_start()
    elif response == '3':
        char = 'ranger'
        Character(name,gen,char)
        adventure_start()
    elif response == '4':
        character_description()
        
        
'''    
pro = Character('Gilroy','m','warrior')
deut = Character()
tert = Character()
ant = Character()

The above variables will instantiate new objects to be used in the game if needed.

'''
def adventure_start():
    global pro
    pro = Character(name,gen,char)
    print(f'Welcome, {name} I see that you are a {pro.char}.  We will need a champion like you if we hope to survive.')
    print('Two areas have been corrupted with a dark evil.')
    response = input('The dragons\'s lair or the castle: ')
    while True:
        if 'dragon' or 'lair' in response.lower():
            pass
            #dragons_lair()
        elif 'castle' or 'cast' in response.lower():
            pass
            #castle()
        else:
            print(f'We cannot do that now, {name}.  Try again')
            


setup()
intro()
gollum = enemy_class.Enemy(50,50,50,50,'morbin time')
print(gollum.getHealth())

