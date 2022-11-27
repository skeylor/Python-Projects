""" Quiz Game (Earth Science) """

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
#doesn't earn any extra points
print('3. Answers are not case-insensitive (uppercase or lowercase works).')
print('4. Do not type additional spaces before or after your answer.')
print('5. If a question is multiple choice, type in only the letter of the')
print('   correct answer.')
print(border)
print('Here come the questions!')
print(border, '\n')

#Question 1
print('1. The four Earth systems are')
print('    A. magnetosphere, ecosphere, atmosphere, cosmosphere  B. atmosphere, hydorsphere, geosphere, biosphere')
print('    C. earth, wind, fire, water                           D. trophosphere, stratosphere, mesosphere, thermosphere')
get_and_check_ans('B')


#Question 2
print('2. The imaginary line running across the Earth horizontally--dividing the Earth into northern and southern hemispheres.')
print('    A. prime meridian    B. equator')
print('    C. longitude         D. latitude')
get_and_check_ans('b')

#Question 3
print('3. Distance in degrees north or south of the equator')
print('    A. latitude          B. longitude')
print('    C. prime meridian    D. Hairy northern Styles')
get_and_check_ans('A')

#Question 4
print('4. A variable whose variation does not depend on that of another.')
print('    A. dependent variable                        B. independent variable')
print('    C. Fermi\'s paradox (where are the aliens?)  D. velocity')
get_and_check_ans('B')

#Question 5
print('5. Choose the option that matches the Greek prefix with the correct meaning.')
print('    A. hydro = dragon    B. atmo = atom')
print('    C. bio = life        D. geo = mars')
get_and_check_ans('C')

#Question 6
print('6. What portion of Earth\'s surface is covered in water?')
print('     A. About 29%       B. About 71%')
print('     C. 97%             D. Earth is a barren wasteland')
get_and_check_ans('B')

#Question 7
print('7. The ________ scale is often used in minerology to measure hardness.')
print('    A. Faraday\'s       B. Newton\'s')
print('    C. Ohm\'s           D. Mohs')
get_and_check_ans('D')

#Having more than 7 questions is an enhancement:

#Question 8
print('8. The four characteristics of a mineral include being')
print('solid, crystal structure, definite chemical makeup, and _________.')
print('     A. forms in the nebula    B. forms in nature')
print('     C. has a hardness of 8.0  D. is made of igneous rock.')
get_and_check_ans('B')

#Question 9
print('9. What are the three main types of rocks?')
print('     A. sedimentary, igneous, metamorphic     B. extrusive, intrusive, igneous')
print('     C. rocks, minerals, ores                 D. metal, mineral, solid')
get_and_check_ans('A')

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
print('13. Which kind of rocks form by recrsytallization?')
print('     A. igneous        B. extrusive igneous')
print('     C. metamorphic    D. sedimentary')
get_and_check_ans('C')

#Question 14
print('14. The force of expanding water in the cracks and pores')
print(' of a rock is an example of')
print('     A. chemical weathering   B. mechanical weathering')
print('     C. oxidation             D. desertification')
get_and_check_ans('B')

#Question 15
print('15. What is humus?')
print('     A. The decomposed rock particles in soil     B. The material that makes of the c horizon')
print('     C. The material that makes up the B horizon  D. The decomposed organic matter in soil' )
get_and_check_ans('D')

print('Your final score is', score, 'points out of a possible 150!!')
