
student_name = input('Enter your name: ')

border = '='* 80

print('Welcome to your report card,',student_name + '.')
print('Only input the percentage scores without any symbols.')

'''
Start with a fruitful function to take the subject as an argument.
This function will take the input from the user and return the grade
as a number from 0-100.
'''

def ask_pt_grade(subject):
    print('Enter the percentage score for',subject,end=' ')
    pt_grade = float(input(': '))
    return pt_grade

'''
Reassigning a function's value to a short but descripitve
variable name to make it easier to type.
'''
subjects = int,input(map)
science = ask_pt_grade('Science')
english = ask_pt_grade('English')
math = ask_pt_grade('Math')
computers = ask_pt_grade('Computers')
logic = ask_pt_grade('Logic')
grammar = ask_pt_grade('Grammar')

'''
The following function will take the point grade of a subject and
return the letter grade.  Since the value of the fruitful
function has a numeric value, it can be compared to other
integers and converted and returned as a letter.
'''

def pt_grade_to_letter(pt_grade):
    if pt_grade >= 94:
        return 'A'
    elif 94 > pt_grade >= 90 :
        return 'A-'
    elif 90 > pt_grade >= 87:
        return 'B+'
    elif 87 > pt_grade >= 84:
        return 'B'
    elif 84 > pt_grade >= 80:
        return 'B-'
    elif 80 > pt_grade >= 77:
        return 'C+'
    elif 77 > pt_grade >= 74:
        return 'C'
    elif 74 > pt_grade >= 70:
        return 'C-'
    elif 70 > pt_grade >= 60:
        return 'D'
    else:
        return 'F'
'''
Reassigning a function value to a variable name again.
'''

science_grade = pt_grade_to_letter(science)
english_grade = pt_grade_to_letter(english)
math_grade = pt_grade_to_letter(math)
computers_grade = pt_grade_to_letter(computers)
logic_grade = pt_grade_to_letter(logic)
grammar_grade = pt_grade_to_letter(grammar)


'''
The following function will take the letter grade and convert it
to a point value that is used to measure gpa.
'''

def letter_to_gpa(subject_gpa):
    gp = subject_gpa
    if gp == 'A ':
        return 4.0
    elif gp == 'A-':
        return 3.7
    elif gp == 'B+':
        return 3.3
    elif gp == 'B ':
        return 3.0
    elif gp == 'B-':
        return 2.7
    elif gp == 'C+':
        return 2.3
    elif gp == 'C ':
        return 2.0
    elif gp == 'C-':
        return 1.7
    elif gp =='D ':
        return 1.0
    else:
        return 0.0
    
science_gpa = letter_to_gpa(science_grade)
english_gpa = letter_to_gpa(english_grade)
math_gpa = letter_to_gpa(math_grade)
computers_gpa = letter_to_gpa(computers_grade)
logic_gpa = letter_to_gpa(logic_grade)
grammar_gpa = letter_to_gpa(grammar_grade) 





border = '================================================='

print(border)
print('Report card for',student_name)
print(border)
'''
Takes the gpa of all the subjects and puts them in a list.
'''
total_gpa = [science_gpa, english_gpa, math_gpa, computers_gpa, logic_gpa, grammar_gpa]
total = 0
'''
The for loop will iterate through a list starting at index 0 and end once it has
searched the length(len) of the list.  The total variable stores all
of the values in the list added together.
'''

for i in range(0, len(total_gpa)):
    total = total + total_gpa[i]

gpa = total/len(total_gpa)

print()
print()

print(border)
print('Student name: ',student_name)
print(border)

for grade in len(total_gpa):
    print('{}: {:^10}  {:>10}'.format(grade,science_grade,science_gpa))
print('English:   ',english_grade,'         ',english_gpa)
print('Math:      ',math_grade,'          ',math_gpa)
print('Computers: ',computers_grade,'          ',computers_gpa)
print('Logic:     ',logic_grade,'         ',logic_gpa)
print('Grammar:   ',grammar_grade,'         ',grammar_gpa)

print(border)
print('Gpa: ',round(gpa,2))
print(border)

 
