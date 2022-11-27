#String operations

string = 'hello, to everybody out there'

print(string.lower())

print(string.upper())

print(string.capitalize())

# This will only capitalize the first letter in a string

string_list = string.split()

print(string_list)

name = 'sean patrick keylor'

name = ' '.join([f"{i[:1].upper()}{i[1:].lower()}" for i in name.split(' ')])

# This method will split the name at the first letter and uppercase only the first letter
# It also makes sure that all letters to the right of the string are lowercase
# This will work on any number of names in a string and then join the string back together
# at the end.

print(name)

# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))

string = 'ABCDCDC'
substring = 'CDC'

for substring in string:
    print(string.find(substring))
    
    
