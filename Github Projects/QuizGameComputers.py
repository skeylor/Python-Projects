""" Quiz Game (Computers) """

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
print('1. The study of computer science is primarily concerned with:')
print(    'A. evaluating and testing business software.  B. using computers and computer programs to solve problems')
print(    'C. learning programmming languages.           D. designing computers')
get_and_check_ans('B')

#Question 2
print('2. The three main stages data passes through in a program are:')
print(    'A. plan ----> code ----> test         B. input ----> analyze ----> revise')
print(    'C. input ----> output ----> process   D. input ----> process ----> output')
get_and_check_ans('D')

#Question 3
print("3. What is the data type of the value '17.0'?(Note that the quotes are part of the value)")
get_and_check_ans('string')

#Question 4
print('4. The data type of the result of the calculation 8/2 is:')
print(    'A. integer                 B. list')
print(    'C. float                   D. string')
get_and_check_ans('C')

#Question 5
print("5. The code print('hello, world.') is:")
print(     'A. a bug                     B. a string')
print(     'C. a conditional statement   D. an output statement')
get_and_check_ans('D')

#Question 6
print("6. Name1 = 'Bob' is a statement (true or false)")
get_and_check_ans('true')

#Question 7
print('7. Kyle@it is a valid variable name (true or false)')
get_and_check_ans('false')
#Having more than 7 questions is an enhancement:

#Question 8
print('8. What is the best biological analogy for the cpu in a computer')
print(    'A. The cpu is like the heart      B. The cpu is like the brain')
print(    'C. The cpu is like the appendix   D. The cpu is like the nervous system')
get_and_check_ans('B')

#Question 9
print('9. Primary memory is:')
print('     A. also known as RAM                                    B. faster than secondary memory')
print('     C. where the programs load when the computer starts     D. all of the above')
get_and_check_ans('D')

#Question 10
print("10. 3,876 is what kind of data type?")
print('     A. list')
print('     B. string')
print('     C. float')
print('     D. invalid')
get_and_check_ans('A')

#Question 11
print('11. The kind of error that occurs when you forget a quotation mark or parenthesis.')
get_and_check_ans('syntax')


print('Your final score is', score, 'points out of a possible 110!!')
