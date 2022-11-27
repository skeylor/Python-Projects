score = 0
import time, re
border = '====================================================================================='

def quiz_game(cor_ans,points):
    global score
    answer = input('Enter your answer here: ')
    answer = answer.lower()
    cor_ans = cor_ans.lower()
    if answer == cor_ans:
        print('calculating...')
        time.sleep(.5)
        print()
        print('You are correct!!')
        score += points
        print(score)
        print()
    else:
        print('calculating...')
        time.sleep(.5)
        print()
        print('That is incorrect')
        print('Try again')
        print()
        answer = input('Enter your answer here: ')
        answer = answer.lower()
        print()
        if answer == cor_ans:
            print('calculating...')
            time.sleep(.5)
            print()
            print('You got it!!')
            score += (int(points/2))
            print(score)
            print()
        else:
            print("Sorry, that's not right")
            print()
            
            
           


        
print('1.) What was the name of the first electronic digital')
print('programmable computer?\n')

print('a. The BOMBE               b. The Apple II')
print('c. The Colossus Mark I     d. The difference engine')


quiz_game('c',10)
print()
print(border)
print()



print("2.) Considered to be the 'father of the computer',")
print('this polymath originated the concept of a programmable')
print('computer in the early nineteenth century in England.\n')

print('a. Joseph Jacquard         b. Blaise Pascal')
print('c. Steve Jobs              d. Charles Babbage')




quiz_game('d',10)
print()
print(border)
print()




print('3.) This famous mathematician is considered to be the')
print('first computer programmer for working with the analytical')
print('engine and creating the first published algorithm. \n')

print('a. Mary Shelley            b. Ada Lovelace')
print('c. Mark Zuckerberg         d. Steve Wozniak')



quiz_game('b',20)
print()
print(border)
print()
print('Want to know a fun fact about Ada Lovelace?')
response = input('Enter your answer here: ')
response_list = ['yeah','yes','okay','ok','affirmative','sure','ye','fine']
if response in response_list:
    print('Ada Lovelace is the daughter of Lord Byron, who was famous for his')
    print('involvement with Romanticism and association with other popular writers')
    print('like Percy Bysshe Shelley and Mary Shelley.')
    time.sleep(8)
    print()



print('4.) The principle of the modern computer was proposed')
print('by this genius mathematician who also helped defeat')
print("the Nazis in Germany by cracking the 'unbreakable' enigma code.\n")

print('a. Alan Turing             b. Larry Page')
print('c. David Packard           d. Bill Hewlitt')



quiz_game('a',10)
print()
print(border)
print()
print('Want to know more about Alan Turing?')
response = input('Enter your answer here: ')
if response in response_list:
    print('Not only was Turing a great mathematician, he was also a computer scientist,')
    print('logician, cryptanalyst, philosopher, and theoretical biologist.')
    print('Turing is credited with providing a formalisation of the concepts')
    print('of algorithm and computation.  He is still widely considered to be the father of')
    print('theoretical computer science and artificial intelligence.')
    time.sleep(10)
    print()


print('5.) The ENIAC, which came after the Mark I, was the')
print('first programmable, electronic, general-purpose digital computer')
print('made in 1945.  What does ENIAC stand for?\n')

print('a. Electrical Numeric Intelligence Artificial Computer')
print('b. Everyone Nose I Am Complicated')
print('c. Electronic Numerical Integrator and Computer')
print('d. Electrical Numberic Internet and Calculator')




quiz_game('c',15)
print()
print(border)
print()
print('Do you want to know more about the Mark I?')
response = input('Enter your answer here: ')
if response in response_list:
    print('The Mark I used vacuum tubes to represent 1\'s and 0\'s.')
    print('These vacuum tubes were inserted into giant plugboards.')
    print('A filament would heat a cathode causing')
    print('it to emit electrons that were attracted to positively charged')
    print('anodes on the other side of a grid in an electric field.')
    print('The ENIAC used manually operated plugs and switches,')
    print('and was faster, more flexible, and')
    print('turing-complete (able to solve "a large class of numerical problems" through reprogramming.')
    time.sleep(8)
    print()


print('6.) These tiny semiconductors replaced vacuum tubes')
print('after 1955 and forever changed the way a computer can')
print('amplify or switch electrical signals and power.\n')

print('a. graphics cards           b. cooling systems')
print('c. motherboards             d. transistors')




quiz_game('d',20)
print()
print(border)
print()




print("7.) Moore's law states that:\n")

print('a. every action has an equal and opposite reaction')
print('b. the number of transistors in a dense integrated circuit doubles about every two years.')
print('c. anything that can go wrong, will go wrong')
print('d. We are just an advanced breed of monkeys on a minor planet of a very average star.')






quiz_game('b',10)
print()
print(border)
print()






print("8.) The term, 'computer bug' originated from: \n")

print('a. An infestation of cockroaches that invaded a cpu factory during WWII.')
print('b. Errors in code resembling small bugs in the machine code.')
print('c. Admiral Grace Hopper encountering a moth in the relay of the Mark II.')
print('d. Alan Turing was an avid bug collector as well as a computer scientist.')




quiz_game('c',10)
print()
print(border)
print()



print('9.) The first working prototype of the internet')
print('came in the late 1960s with the creation of the: \n')

print('a. IBM supercomputer              b. Apple II')
print('c. Fiber optic cables             d. ARPANET')




quiz_game('d',20)
print()
print(border)
print()




print('10.) Who created the first comercially viable graphical user interface?\n')

print('a. Bill Gates at Microsoft            b. Steve Wozniak at Apple')
print('c. Steve Jobs at Apple                d. Some random nerds at Xerox')


quiz_game('d',20)
print()
print(border)
print()





print('11.) Who created the programming language Python?\n')

print('a. Charles Bukowski     b. Guido van Rossum')
print('c. Larry Page           d. Mark Zuckerberg')




quiz_game('b',15)
print()
print(border)
print()



print('12.) How did Python get its name?\n')

print('a. The creator is an avid reptile enthusiast')
print('b. The creator got bit by a python as a child and has been wheelchair bound ever since.')
print("c. The creator is a huge fan of Monty Python's Flying Circus")
print('d. The creator has a python for an arm')






quiz_game('c',10)
print()
print(border)
print()





print('13.) What will the following expression return: (5**2 + 12/2 - 30)')







quiz_game('1.0',20)
print()
print(border)
print()



print('14.) What kind of programming language is Python?\n')

print('a.object oriented programming language      b. scripting programming language')
print('c.low level programming language            d. a reptile....duh')







quiz_game('a',15)
print()
print(border)
print()





print('15.)Which of the following languages is not usually')
print('used for building websites?\n')

print('a. HTML              b. CSS')
print('c. javascript        d. C++')





quiz_game('d',10)

def quiz_game(cor_ans,points):
    global score
    answer = input('Enter your answer here: ')
    if answer in cor_ans:
        print('You are correct!!')
        score += points
        print(score)
    else:
        print('That is incorrect')
        
print('16.)Name an object oriented programming language.\n Use lower case letters.')
quiz_game(['c++','c#','ruby','python','java','javascript'],10)


if score == 225:
    print('You got every answer right you absolute legend.')
elif score < 225 and score > 200:
    print('Well done!!')
elif score < 200 and score > 150:
    print('Not bad for a rookie')
else:
    print('You have some studying to do')



print(score,'out of 225 possible points.')
print()
print('Good game.  Press f5 to play again.')
print(border)
print()
