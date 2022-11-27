""" Quiz Game (Physical Science) """

#Key Variables
border = '————————————————————————————————————————————————————————————————————————'
score = 0

#As an enhancement, students can replace their repetitive conditionals with
#some version of the following function. They can also modify the code to
#give players extra chances to answer questions (for lower point rewards).
#
#get_and_check_ans() will get the user's answer as input and compare it to
#the correct answer (cor_ans). It will give the user an additional attempt
#if necessary and award points accordingly. cor_ans must be passed into
#this function as a string, or else an error will result.
#
def get_and_check_ans(cor_ans):
    global score
    ans = input()
    cor_ans = cor_ans.lower()   #Make both the correct answer and the user's
    ans = ans.lower()           #answer lowercase for easy comparison (optional)
    #Check if the user's answer is correct and award points accordingly:
    if ans == cor_ans:
        print('That is correct! Well done!')
        print('You earn 10 points.')
        score = score + 10
    else:
        print('That is incorrect! Please try again:')  #Offer a second chance
        ans = input().lower()                          #to answer question
        if ans == cor_ans:
            print('That is correct. You earn 5 points.')  #Lower reward for
            score = score + 5                             #second attempt
        else:
            print('I\'m sorry, that is incorrect.')
    print()

#Introduction and Rules
print('Welcome to The Quiz Game!!')
print(border)
print('In this game, you will be given a series of trivia and math questions.')
print('Type in your answer to each followed by Enter. See the rules below.')
print(border)
print('Rules:')
print('1. You will receive two tries to answer each question. If you answer')
print('   correctly on the first try, you earn 10 points. 2nd try: 5 points.')
print('   Otherwise: 0 points.')
print('2. Incorrectly spelled answers are not accepted.')
#Making answers case-insensitive is a design choice; it's not required and
#doesn\'t earn any extra points
print('3. Answers are not case-insensitive (uppercase or lowercase works).')
print('4. Do not type additional spaces before or after your answer.')
print('5. If a question is multiple choice, type in only the letter of the')
print('   correct answer.')
print(border)
print('Here come the questions!')
print(border, '\n')

#Question 1
print('1. Anything that has mass and takes up space is called?')
get_and_check_ans('matter')

#Question 2
print('2. How much matter an object contains is called this')
get_and_check_ans('mass')

#Question 3
print('3. The downward pull on an object due to gravity is called what?')
print('    A. matter        C. mass')
print('    B. weight        D. height')
get_and_check_ans('B')

#Question 4
print('4. Put in order from smallest to largest: separate answers with a comma')
print('    A. molecules               C. atoms')
print('    B. subatomic particles     D. cells')
get_and_check_ans('B,C,A,D')

#Question 5
print('5. The formula for finding volume is V = lwh.')
print('L stands for length and the w stands for width.  What does h stand for?')
get_and_check_ans('height')

#Question 6
print('6. What are atoms made up of?')
print('     A. quantum, plasma, electricity    B. subatomic particles')
print('     C. protons, neutrinos, electrons   D. quarks, gluons, plancks')
get_and_check_ans('B')

#Question 7
print('7. The three common states of matter are:')
print('    A. plasma, liquid, solid     C. compound, molecular, atomic')
print('    B. solid, liquid, gas        D. matter is subjective and therefore unanswerable')
get_and_check_ans('B')

#Having more than 7 questions is an enhancement:

#Question 8
print('8. If a faucet can fill a water tank in 8 hours, and a drain pipe can')
print('   fully drain the tank in 6 hours, how many hours will it take to')
print('   drain the tank from full to empty while the faucet is on at the')
print('   same time? Enter just the number without units.')
get_and_check_ans('24')

#Question 9
print('9. Compounds can only be separated by breaking their what?')
print('     A. atoms     C. molecules')
print('     B. bonds     D. hearts   ')
get_and_check_ans('B')

#Question 10
print('10. This is the process by which a liquid turns into a gas:')
print('     A. surface runoff')
print('     B. condensation')
print('     C. evaporation')
print('     D. precipitation')
get_and_check_ans('C')

#Question 11
print('11. When a solid changes directly into a gas without first')
print(' changing to a liquid, it is an example of this:')
get_and_check_ans('sublimation')

#Question 12
print('12. Also a legal term, in chemistry it is when a gas changes')
print(' directly into a solid.')
get_and_check_ans('deposition')

#Question 13
print('13. The law that states that energy cannot be destroyed,')
print(' nor can it be created is known as:')
print('     A. law of conservation of energy   C. Newton\'s law')
print('     B. law of conservation of mass     D. Ohm\'s law   ')
get_and_check_ans('A')

#Question 14
print('14. This term used in nutrition is also the amount of energy')
print(' needed to raise the temp. of 1 g of water 1 degree celcius.')
get_and_check_ans('calorie')


#Question 15
print('15. Conductors are relative to two different areas of energy')
print(' which enable them to easily transfer ________ and ________.')
print('     A. temperature, electrodes           C. heat, electricity')
print('     B. kinetic energy, potential energy  D. batman and robin' )
get_and_check_ans('C')

print('Your final score is', score, 'points out of a possible 150!!')
if score >= 130:
    print('Wow, impressive work.  I see you know your science.')
elif score < 130 and score > 80:
    print('Solid effort.')
else:
    print('You have some studying to do.')