'''
vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWYZ'
vowel_list = []
cons_list = []
s="BANANA"
s=set(s)
s="".join(s)
new_string =""
for letter in s:
    if letter in vowels:
        vowel_list.append(letter)      
    else:
        cons_list.append(letter)
vowel_list = ''.join(vowel_list)
cons_list = ''.join(cons_list)

stuart = 0
kevin = 0
string = 'BANANA'
new_strings=""
for letter in string:
    if letter in s:
        print(letter)
    else:
        new_strings = new_strings + vowel_list
    print(new_strings)

'''

def removeDuplicate(str):
    s=set(str)
    s="".join(s)
    vowels = 'AEIOU'
    consonants = 'BCDFGHJKLMNPQRSTVWYZ'
    vowel_list = []
    cons_list = []
    for letter in s:
        if letter in vowels:
            vowel_list.append(letter)      
        else:
            cons_list.append(letter)
    vowel_words = []
    cons_words = []
    for letter in vowel_list:
        print(letter)
    for letter in cons_list:
        print(letter)
    for letter in str:
            pass
        else:
            t=t+i
            print("With Order:",t)
    print(t)
     
str="BANANA"
removeDuplicate(str)